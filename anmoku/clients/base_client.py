from __future__ import annotations
from typing import TypedDict

__all__ = ("ConfigDict", "BaseClient")

class ConfigDict(TypedDict):
    headers: dict
    jikan_url: str

class BaseClient():
    """Base class all clients will inherit from."""
    def __init__(self, config: ConfigDict = None) -> None:
        ...