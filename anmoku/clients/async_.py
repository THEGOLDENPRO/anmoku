from __future__ import annotations

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

        self._session: Optional[ClientSession] = None

    def recreate(self) -> ClientSession:
        if self._session is None:
            self._session = ClientSession(self._api_url)

        return self._session

    async def close(self) -> None:
        if self._session is None:
            return
        
        await self._session.close()
        self._session = None

    async def request(
        self, 
        route: str, 
        *, 
        query: Optional[dict[str, Any]] = None, 
        headers: Optional[dict[str, str]] = None
    ):
        session = self.recreate()
        headers = headers or {}
        combined_headers = {**headers, **self._headers}

        # TODO: rate limits
        # There are two rate limits: 3 requests per second and 60 requests per minute.
        # In order to comply, we need to check the 60 requests per minute bucket first, then the 3 requests per second one.
        async with session.get(route, params=query, headers=combined_headers) as resp:
            resp.raise_for_status()

            content = await resp.text()
            return (content, resp.headers)
