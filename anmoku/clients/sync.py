from __future__ import annotations

from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Any, Optional, TypeVar

    from ..typing.anmoku import Snowflake
    from ..resources import JikanResource

    A = TypeVar(
        "A", 
        bound = JikanResource
    )

from requests import Session
from devgoldyutils import Colours

from .base import BaseClient

__all__ = ("Anmoku",)


class Wrapper():
    """Anmoku api wrapper for the normal client."""

    def get(self: Anmoku, resource: type[A], id: Snowflake) -> A:
        """Get's the object by id."""
        url = resource._get_endpoint.format(id = id)

        json_data = self._request(url)

        return resource(json_data)

class Anmoku(BaseClient, Wrapper):
    """The normal synchronous Anmoku client."""

    __slots__ = (
        "_session",
    )

    def __init__(
        self, 
        debug: Optional[bool] = False, 
        jikan_url: Optional[str] = None,
        session: Optional[Session] = None
    ) -> None:
        super().__init__(debug)

        self.jikan_url = jikan_url or "https://api.jikan.moe/v4"
        self._session = session

    def _request(
        self, 
        route: str, 
        *, 
        query: Optional[dict[str, Any]] = None, 
        headers: Optional[dict[str, str]] = None
    ) -> dict[str, Any]:
        headers = headers or {}

        session = self.__get_session()
        url = self.jikan_url + route

        # TODO: rate limits
        # There are two rate limits: 3 requests per second and 60 requests per minute.
        # In order to comply, we need to check the 60 requests per minute bucket first, then the 3 requests per second one.
        self.logger.debug(f"{Colours.GREEN.apply('GET')} --> {url}")

        with session.get(url, params = query, headers = headers) as resp:
            content = resp.json()

            if resp.status_code > 400:
                self._raise_http_error(content, resp.status_code)

            return content

    async def close(self) -> None:
        if self._session is None:
            return
        
        await self._session.close()
        self._session = None

    def __get_session(self) -> Session:
        if self._session is None:
            self._session = Session()

        return self._session