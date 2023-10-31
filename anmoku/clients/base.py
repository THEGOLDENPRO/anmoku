from __future__ import annotations

from typing import Any, Optional, TypedDict

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
