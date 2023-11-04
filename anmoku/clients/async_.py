from __future__ import annotations

from typing import TYPE_CHECKING, TypeVar, Type

if TYPE_CHECKING:
    from typing import Any, Optional

    from .base import ConfigDict
    from ..typing.anmoku import Snowflake
    from ..objects import Anime, Character

    T = TypeVar("T", Type[Anime], Type[Character])

from devgoldyutils import Colours
from aiohttp import ClientSession
from json import loads as load_json

from .base import BaseClient

__all__ = ("AsyncAnmoku",)


class AsyncWrapper():
    """Anmoku api wrapper for the async client."""
    def __init__(self) -> None:
        ...

    async def get(self, object: T, id: Snowflake) -> T: 
        """Get object by id."""
        # TODO: Find a more suitable name other than "object".

        json_data = await self._request(object._endpoint + f"/{id}")

        return object(json_data)

class AsyncAnmoku(BaseClient, AsyncWrapper):
    """Asynchronous anmoku client."""

    __slots__ = (
        "_session",
    )

    def __init__(
        self, 
        config: Optional[ConfigDict] = None, 
        aiohttp_session: Optional[ClientSession] = None
    ) -> None:
        super().__init__(config)

        self._session = aiohttp_session

    async def _request(
        self, 
        route: str, 
        *, 
        query: Optional[dict[str, Any]] = None, 
        headers: Optional[dict[str, str]] = None
    ):
        headers = headers or {}
        combined_headers = {**headers, **self.config["headers"]}

        session = self.__get_session()
        url = self.config["jikan_url"] + route

        # TODO: rate limits
        # There are two rate limits: 3 requests per second and 60 requests per minute.
        # In order to comply, we need to check the 60 requests per minute bucket first, then the 3 requests per second one.
        self.logger.debug(f"{Colours.GREEN.apply('GET')} --> {url}")
        async with session.get(url, params=query, headers=combined_headers) as resp:
            content = await resp.text()

            if resp.content_type == "application/json":
                content = load_json(content)
            else:
                raise ValueError(f"Expected json response, got {resp.content_type}")

            if resp.status > 400:
                self._raise_http_error(content, resp.status)

            return content
        
    async def close(self) -> None:
        if self._session is None:
            return
        
        await self._session.close()
        self._session = None

    def __get_session(self) -> ClientSession:
        if self._session is None:
            self._session = ClientSession()

        return self._session
