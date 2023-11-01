from __future__ import annotations
from typing import TYPE_CHECKING

from json import loads as load_json

if TYPE_CHECKING:
    from typing import Any, Optional

from aiohttp import ClientSession

from .base import BaseClient, ConfigDict

__all__ = ("AsyncAnmoku",)

class AsyncAnmoku(BaseClient):
    """Asynchronous anmoku client."""

    __slots__ = (
        "_session",
    )

    def __init__(self, config: Optional[ConfigDict] = None) -> None:
        super().__init__(config)

        self._api_url: str = config["jikan_url"]

        self._session: Optional[ClientSession] = None

    async def request(
        self, 
        route: str, 
        *, 
        query: Optional[dict[str, Any]] = None, 
        headers: Optional[dict[str, str]] = None
    ):
        headers = headers or {}
        combined_headers = {**headers, **self.config["headers"]}

        session = self.__get_session()

        # TODO: rate limits
        # There are two rate limits: 3 requests per second and 60 requests per minute.
        # In order to comply, we need to check the 60 requests per minute bucket first, then the 3 requests per second one.
        async with session.get(self._api_url + route, params=query, headers=combined_headers) as resp:
            content = await resp.text()

            if resp.content_type == "application/json":
                content = load_json(content)
            else:
                raise ValueError(f"Expected json response, got {resp.content_type}")

            self._raise_http_error(content, resp.status)

            return content
        
    async def close(self) -> None:
        if self._session is None:
            return
        
        await self._session.close()
        self._session = None

    def __get_session(self) -> ClientSession:
        if self._session is None:
            self._session = ClientSession(self._api_url)

        return self._session
