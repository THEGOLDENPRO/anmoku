from __future__ import annotations
from typing import TYPE_CHECKING, cast, Optional

if TYPE_CHECKING:
    from typing import Any, Mapping, TypeVar
    from .. import resources as r

    ResourceGenericT = TypeVar(
        "ResourceGenericT", 
        bound = r.JikanResource
    )

    SearchResourceGenericT = TypeVar(
        "SearchResourceGenericT", 
        r.Anime, 
        r.Character,
    )

import logging
from abc import ABC
from devgoldyutils import LoggerAdapter

from ..logger import anmoku_logger
from .rate_limiting import RateLimitHandler
from ..errors import ErrorResponseDict, NotFoundError, RatelimitError, ServerError, HTTPError

__all__ = ("BaseClient",)

class BaseClient(ABC):
    """Base class all clients will inherit from."""

    __slots__ = (
        "logger",
        "cache",
    )

    def __init__(
        self, 
        debug: bool, 
        wait: bool, 
        max_retries: int, 
        requests_per_second_limit: Optional[int] = None, 
        requests_per_minute_limit: Optional[int] = None
    ) -> None:

        if debug is True:
            anmoku_logger.setLevel(logging.DEBUG)

        self.logger = LoggerAdapter(anmoku_logger, prefix = self.__class__.__name__)

        self.wait = wait
        self.max_retries = max_retries

        self._rate_limit_handler = RateLimitHandler(requests_per_second_limit, requests_per_minute_limit)

        self.__retries = 0

        super().__init__()

    def _raise_http_error(self, data: Mapping[str, Any], status: int):
        data = cast(ErrorResponseDict, data)

        if status == 404:
            raise NotFoundError(data)
        elif status == 429:
            raise RatelimitError(data)
        elif status >= 500:
            raise ServerError(data)

        raise HTTPError(data)

    def _retry(self, status_code: int) -> bool:
        if self.wait and status_code == 429 and not self.__retries >= self.max_retries:
            self.__retries += 1
            return True

        self.__retries = 0
        return False