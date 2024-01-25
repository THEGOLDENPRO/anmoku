from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Optional, Type

    from ..typing.anmoku import Snowflake
    from ..typing.jikan import SearchResultData

    from .base import ResourceGenericT, SearchResourceGenericT

from devgoldyutils import Colours
from aiohttp import ClientSession

from .. import errors, logger
from ..resources.helpers import SearchResult

from .base import BaseClient

__all__ = ("AsyncAnmoku",)

class AsyncWrapper():
    """Anmoku api wrapper for the async client."""

    async def get(self: AsyncAnmoku, resource: Type[ResourceGenericT], id: Snowflake) -> ResourceGenericT:
        """Get's the exact resource by id."""
        url = resource._get_endpoint.format(id = id)

        json_data = await self._request(url)

        return resource(json_data)

    async def search(self: AsyncAnmoku, resource: Type[SearchResourceGenericT], query: str) -> SearchResult[SearchResourceGenericT]:
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
        debug: bool = False, 
        session: Optional[ClientSession] = None,
        jikan_url: str = "https://api.jikan.moe/v4",
        max_retries: int = 10,
        wait: bool = True
    ) -> None:
        super().__init__(debug, wait, max_retries)

        self._session = session

        self.jikan_url = jikan_url

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
        logger.log_http_request("GET", url, logger = self.logger)

        async with session.get(url, params = params, headers = headers) as resp:
            content = await resp.json()

            if self.wait:
                await self._rate_limit_handler.async_wait_for_rate_limit()

            if self._retry(resp.status):
                self.logger.debug(f"{Colours.GREY.apply('Retrying')} request to '{url}'...")
                content = await self._request(route, params = params, headers = headers)

            elif resp.status > 400:
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