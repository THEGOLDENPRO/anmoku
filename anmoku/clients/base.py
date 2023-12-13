from __future__ import annotations
from typing import TYPE_CHECKING, cast

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
from ..errors import ErrorResponseDict, NotFoundError, RatelimitError, ServerError, HTTPError

__all__ = ("BaseClient",)


class BaseClient(ABC):
    """Base class all clients will inherit from."""

    __slots__ = (
        "logger",
        "cache",
    )

    def __init__(self, debug: bool = False) -> None:

        if debug is True:
            anmoku_logger.setLevel(logging.DEBUG)

        self.logger = LoggerAdapter(anmoku_logger, prefix = self.__class__.__name__)

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
