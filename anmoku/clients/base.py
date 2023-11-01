from __future__ import annotations

from typing import Any, Mapping, Optional, TypedDict, cast

from .errors import ErrorResponseDict, NotFoundError, RatelimitError, ServerError, HTTPError

__all__ = ("ConfigDict", "BaseClient")

DEFAULT_API_URL = "https://api.jikan.moe/v4"

class ConfigDict(TypedDict):
    headers: dict[str, Any]
    jikan_url: str


class BaseClient:
    """Base class all clients will inherit from."""

    __slots__ = (
        "_headers",
        "_api_url",
        "cache",
    )

    def __init__(self, config: Optional[ConfigDict] = None) -> None:
        self._headers: dict[str, Any] = config["headers"] if config is not None else {}
        self._api_url: str = config["jikan_url"] if config is not None else DEFAULT_API_URL

    def _raise_http_error(self, data: Mapping[str, Any], status: int):
        data = cast(ErrorResponseDict, data)

        if status == 404:
            raise NotFoundError(data)
        elif status == 429:
            raise RatelimitError(data)
        elif status >= 500:
            raise ServerError(data)

        raise HTTPError(data)
