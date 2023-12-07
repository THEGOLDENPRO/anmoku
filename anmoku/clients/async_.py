from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Optional, TypeVar, Type

    from ..typing.anmoku import Snowflake
    from ..typing.jikan import SearchResultData

    from ..resources import JikanResource

    A = TypeVar(
        "A", 
        bound = JikanResource
    )

from devgoldyutils import Colours
from aiohttp import ClientSession
from json import loads as load_json

from .. import errors
from ..resources.helpers import SearchResult

from .base import BaseClient

__all__ = ("AsyncAnmoku",)


class AsyncWrapper():
    """Anmoku api wrapper for the async client."""

    async def get(self: AsyncAnmoku, resource: Type[A], id: Snowflake) -> A:
        """Get's the exact resource by id."""
        url = resource._get_endpoint.format(id = id)

        json_data = await self._request(url)

        return resource(json_data)

    async def search(self: AsyncAnmoku, resource: Type[A], query: str) -> SearchResult[A]:
        """Searches for the resource and returns a list of the results."""
        url = resource._search_endpoint

        if url is None:
            raise errors.ResourceNotSupportedError(resource, "searching")

        json_data: SearchResultData[Any] = await self._request(url, params = {"q": query})

        return SearchResult(json_data, resource)

class AsyncAnmoku(BaseClient, AsyncWrapper):
    """Asynchronous Anmoku client."""

    __slots__ = (
        "_session",
    )

    def __init__(
        self, 
        debug: Optional[bool] = False, 
        jikan_url: Optional[str] = None,
        session: Optional[ClientSession] = None
    ) -> None:
        super().__init__(debug)

        self.jikan_url = jikan_url or "https://api.jikan.moe/v4"
        self._session = session

    async def _request(
        self, 
        route: str, 
        *, 
        params: Optional[dict[str, Any]] = None, 
        headers: Optional[dict[str, str]] = None
    ) -> dict[str, Any]:
        headers = headers or {}

        session = self.__get_session()
        url = self.jikan_url + route

        # TODO: rate limits
        # There are two rate limits: 3 requests per second and 60 requests per minute.
        # In order to comply, we need to check the 60 requests per minute bucket first, then the 3 requests per second one.
        self.logger.debug(f"{Colours.GREEN.apply('GET')} --> {url}")

        async with session.get(url, params = params, headers = headers) as resp:
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