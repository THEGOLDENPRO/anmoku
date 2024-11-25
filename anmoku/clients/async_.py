from __future__ import annotations
from typing import TYPE_CHECKING, overload

if TYPE_CHECKING:
    from typing import Any, Optional, Type, Dict, Tuple

    from ..typing.anmoku import StrOrIntT
    from ..typing.jikan import SearchResultData

    from .base import (
        ResourceGenericT, 
        SearchResourceGenericT, 
        RandomResourceGenericT, 
        NoArgsResourceGenericT
    )

from aiohttp import ClientSession
from devgoldyutils import Colours
from json import loads as load_json
from slowstack.asynchronous.all import AllRateLimiter
from slowstack.asynchronous.times_per import TimesPerRateLimiter

from .base import BaseClient
from ..resources.helpers import SearchResult
from ..errors import ResourceNotSupportedError

__all__ = ("AsyncAnmoku",)

class AsyncAnmoku(BaseClient):
    """
    Asynchronous anmoku client. Uses aiohttp for http and `slowstack`_ for rate-limiting.

    .. _slowstack: https://github.com/TAG-Epic/slowstack
    """

    __slots__ = (
        "_session",
        "jikan_url",
        "_rate_limiter"
    )

    def __init__(
        self,
        debug: Optional[bool] = False,
        jikan_url: Optional[str] = None,
        session: Optional[ClientSession] = None,
        rate_limits: Optional[Tuple[Tuple[int, int], Tuple[int, int]]] = None
    ) -> None:
        super().__init__(debug)

        self.jikan_url = jikan_url or "https://api.jikan.moe/v4"
        self._session = session

        if rate_limits is None:
            # https://docs.api.jikan.moe/#section/Information/Rate-Limiting
            rate_limits = ((3, 3), (60, 60))

        self._rate_limiter = AllRateLimiter(
            {
                TimesPerRateLimiter(limit, per) for (limit, per) in rate_limits
            }
        )

    @overload
    async def get(self, resource: Type[NoArgsResourceGenericT]) -> NoArgsResourceGenericT:
        ...

    @overload
    async def get(self, resource: Type[ResourceGenericT], id: StrOrIntT, **kwargs) -> ResourceGenericT:
        ...

    async def get(self, resource: Type[ResourceGenericT], id: Optional[StrOrIntT] = None, **kwargs) -> ResourceGenericT:
        """Get's the exact resource typically by id."""
        if id is not None:
            kwargs["id"] = id

        url = self._format_url(
            resource._get_endpoint, resource, **kwargs
        )

        json_data = await self._request(url)

        return resource(json_data)

    async def search(self, resource: Type[SearchResourceGenericT], query: str, sfw: bool = True) -> SearchResult[SearchResourceGenericT]:
        """Searches for the resource and returns a list of the results."""
        url = resource._search_endpoint

        if url is None:
            raise ResourceNotSupportedError(resource, "searching")

        json_data: SearchResultData[Any] = await self._request(url, params = {"q": query, "sfw": str(sfw).lower()})

        return SearchResult(json_data, resource)

    async def random(self, resource: Type[RandomResourceGenericT]) -> RandomResourceGenericT:
        """Fetches a random object of the specified resource."""
        url = resource._random_endpoint

        if url is None:
            raise ResourceNotSupportedError(resource, "random")

        json_data = await self._request(url)

        return resource(json_data)

    async def _request(
        self, 
        route: str, 
        *, 
        params: Optional[dict[str, Any]] = None, 
        headers: Optional[dict[str, str]] = None
    ) -> Dict[str, Any]:
        headers = headers or {}

        session = self.__get_session()
        url = self.jikan_url + route

        async with self._rate_limiter.acquire():
            self.logger.debug(f"{Colours.GREEN.apply('GET')} --> {url}")

            async with session.get(url, params = params, headers = headers) as resp:
                self.logger.debug(f"Complete URL: '{resp.url}'")

                content = await resp.text()

                if not resp.content_type == "application/json":
                    raise ValueError(f"Expected json response, got '{resp.content_type}'.")

                content = load_json(content)

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