from __future__ import annotations

from typing import Any, Mapping, Optional, TypedDict, cast

from .errors import ErrorResponseDict, NotFoundError, RatelimitError, ServerError, HTTPError

from abc import ABC

__all__ = ("ConfigDict", "BaseClient")

DEFAULT_API_URL = "https://api.jikan.moe/v4"
DEFAULT_CONFIG: ConfigDict = {
    "headers": {},
    "jikan_url": DEFAULT_API_URL,
}

class ConfigDict(TypedDict):
    headers: dict[str, Any]
    jikan_url: str


class BaseClient(ABC):
    """Base class all clients will inherit from."""

    __slots__ = (
        "config",
        "cache",
    )

    def __init__(self, config: Optional[ConfigDict] = None) -> None:
        self.config: ConfigDict = config if config is not None else DEFAULT_CONFIG

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
