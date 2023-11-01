from __future__ import annotations

from typing import Any, Mapping, Optional, TypedDict, cast

from .errors import ErrorResponseDict, NotFoundError, RatelimitError, ServerError, HTTPError

from abc import ABC, abstractmethod

__all__ = ("ConfigDict", "BaseClient")

DEFAULT_API_URL = "https://api.jikan.moe/v4"

class ConfigDict(TypedDict):
    headers: dict[str, Any]
    jikan_url: str


class BaseClient(ABC):
    """Base class all clients will inherit from."""

    __slots__ = (
        "cache",
    )

    def __init__(self, config: Optional[ConfigDict] = None) -> None:
        self.config: ConfigDict = config if config is not None else {
            "headers": {},
            "jikan_url": DEFAULT_API_URL
        }

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

    @abstractmethod
    def request(
        self, 
        route: str, 
        *, 
        query: Optional[dict[str, Any]] = None, 
        headers: Optional[dict[str, str]] = None
    ):
        ...

    @abstractmethod
    def close(self) -> None:
        ...
