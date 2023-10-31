from __future__ import annotations
from typing import Any, Optional, TypedDict

from abc import ABC, abstractmethod

__all__ = ("ConfigDict", "BaseClient")

DEFAULT_API_URL = "https://api.jikan.moe/v4"

class ConfigDict(TypedDict):
    headers: dict[str, Any]
    jikan_url: str


class BaseClient(ABC):
    """Base class all clients will inherit from."""

    __slots__ = (
        "_headers",
        "_api_url",
        "cache",
    )

    def __init__(self, config: Optional[ConfigDict] = None) -> None:
        self._headers: dict[str, Any] = config["headers"] if config is not None else {}
        self._api_url: str = config["jikan_url"] if config is not None else DEFAULT_API_URL

        super().__init__()

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