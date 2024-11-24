from __future__ import annotations
from typing import TYPE_CHECKING, cast

if TYPE_CHECKING:
    from typing import Any, Mapping, TypeVar, Type

    from .. import resources
    from ..typing.anmoku import SnowflakeT
    from ..resources.helpers import SearchResult

    ResourceGenericT = TypeVar(
        "ResourceGenericT", 
        bound = resources.JikanResource
    )

    SearchResourceGenericT = TypeVar(
        "SearchResourceGenericT", 
        resources.Anime,
        resources.Character,
        resources.Manga
    )

import logging
from urllib.parse import quote
from abc import ABC, abstractmethod
from devgoldyutils import LoggerAdapter

from ..logger import anmoku_logger
from ..errors import (
    ErrorResponseDict,
    NotFoundError,
    RatelimitError,
    ServerError,
    HTTPError,
    ResourceRequiresError
)

__all__ = ("BaseClient",)


class BaseClient(ABC):
    """Base class all clients will inherit from."""

    __slots__ = (
        "logger",
        "cache",
    )

    def __init__(self, debug: bool = False) -> None:
        self.logger = LoggerAdapter(
            anmoku_logger, prefix = self.__class__.__name__
        )

        if debug is True:
            self.logger.setLevel(logging.DEBUG)

        super().__init__()

    @abstractmethod
    def get(self, resource: Type[ResourceGenericT], id: SnowflakeT) -> ResourceGenericT:
        """Get's the exact resource by id."""
        ...

    @abstractmethod
    def search(self, resource: Type[SearchResourceGenericT], query: str) -> SearchResult[SearchResourceGenericT]:
        """Searches for the resource and returns a list of the results."""
        ...

    def _format_url(self, unformatted_url: str, resource: Type[ResourceGenericT], *args: str, **kwargs: str) -> str:
        """Formats the URL while also taking URL encoding into account."""
        try:
            formatted_url = unformatted_url.format(*args, **kwargs)
        except KeyError as e:
            raise ResourceRequiresError(resource, e.args[0])

        return quote(formatted_url)

    def _raise_http_error(self, data: Mapping[str, Any], status: int):
        data = cast(ErrorResponseDict, data)

        if status == 404:
            raise NotFoundError(data)
        elif status == 429:
            raise RatelimitError(data)
        elif status >= 500:
            raise ServerError(data)

        raise HTTPError(data)