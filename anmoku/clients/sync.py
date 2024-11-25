from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Optional, Type, Tuple

    from ..typing.anmoku import SnowflakeT
    from ..typing.jikan import SearchResultData

    from .base import ResourceGenericT, SearchResourceGenericT, RandomResourceGenericT

from requests import Session
from devgoldyutils import Colours
from slowstack.synchronous.times_per import TimesPerRateLimiter

from .base import BaseClient
from ..resources.helpers import SearchResult
from ..errors import ResourceNotSupportedError

__all__ = ("Anmoku",)

class Anmoku(BaseClient):
    """
    The normal synchronous Anmoku client. Uses requests for http and `slowstack`_ for rate limiting.

    .. _slowstack: https://github.com/TAG-Epic/slowstack
    """

    __slots__ = (
        "_session",
        "jikan_url",
        "_second_rate_limiter",
        "_minute_rate_limiter"
    )

    def __init__(
        self,
        debug: Optional[bool] = False,
        jikan_url: Optional[str] = None,
        session: Optional[Session] = None,
        rate_limits: Optional[Tuple[Tuple[int, int], Tuple[int, int]]] = None
    ) -> None:
        super().__init__(debug)

        self.jikan_url = jikan_url or "https://api.jikan.moe/v4"
        self._session = session

        if rate_limits is None:
            # https://docs.api.jikan.moe/#section/Information/Rate-Limiting
            rate_limits = ((3, 3), (60, 60))

        second_rate_limits, minute_rate_limits = rate_limits

        self._second_rate_limiter = TimesPerRateLimiter(second_rate_limits[0], second_rate_limits[1])
        self._minute_rate_limiter = TimesPerRateLimiter(minute_rate_limits[0], minute_rate_limits[1])

    def get(self, resource: Type[ResourceGenericT], id: SnowflakeT, **kwargs) -> ResourceGenericT:
        """Get's the exact resource by id."""
        url = self._format_url(
            resource._get_endpoint, resource, id = id, **kwargs
        )

        json_data = self._request(url)

        return resource(json_data)

    def search(self, resource: Type[SearchResourceGenericT], query: str) -> SearchResult[SearchResourceGenericT]:
        """Searches for the resource and returns a list of the results."""
        url = resource._search_endpoint

        if url is None:
            raise ResourceNotSupportedError(resource, "searching")

        json_data: SearchResultData[Any] = self._request(url, params = {"q": query})

        return SearchResult(json_data, resource)
    
    def random(self, resource: Type[RandomResourceGenericT]) -> RandomResourceGenericT:
        """Fetches a random object of the specified resource."""
        url = resource._random_endpoint

        if url is None:
            raise ResourceNotSupportedError(resource, "random")

        json_data = self._request(url)

        return resource(json_data)

    def _request(
        self, 
        route: str, 
        *, 
        params: Optional[dict[str, Any]] = None, 
        headers: Optional[dict[str, str]] = None
    ) -> dict[str, Any]:
        headers = headers or {}

        session = self.__get_session()
        url = self.jikan_url + route

        # 'AllRateLimiter' doesn't exist yet for the synchronous portion of slowstack so I '.acquire' for both rate-limiters instead.
        with self._minute_rate_limiter.acquire():

            with self._second_rate_limiter.acquire():

                self.logger.debug(f"{Colours.GREEN.apply('GET')} --> {url}")

                with session.get(url, params = params, headers = headers) as resp:
                    content = resp.json()

                    if resp.status_code > 400:
                        self._raise_http_error(content, resp.status_code)

                return content

    def close(self) -> None:
        if self._session is None:
            return

        self._session.close()
        self._session = None

    def __get_session(self) -> Session:
        if self._session is None:
            self._session = Session()

        return self._session