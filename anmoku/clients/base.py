from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, cast

if TYPE_CHECKING:
    from typing import Any, Optional, Mapping


import logging
from abc import ABC
from devgoldyutils import LoggerAdapter

from ..logger import anmoku_logger
from ..errors import ErrorResponseDict, NotFoundError, RatelimitError, ServerError, HTTPError

__all__ = ("ConfigDict", "BaseClient")

DEFAULT_API_URL = "https://api.jikan.moe/v4"
DEFAULT_CONFIG: ConfigDict = {
    "headers": {},
    "jikan_url": DEFAULT_API_URL,
    "debug": False
}

class ConfigDict(TypedDict):
    headers: dict[str, Any]
    jikan_url: str
    debug: bool


class BaseClient(ABC):
    """Base class all clients will inherit from."""

    __slots__ = (
        "config",
        "cache",
    )

    def __init__(self, config: Optional[ConfigDict] = None) -> None:
        self.config: ConfigDict = {**DEFAULT_CONFIG, **config} if config is not None else DEFAULT_CONFIG

        if self.config["debug"] is True:
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
