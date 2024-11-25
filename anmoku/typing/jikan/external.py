from __future__ import annotations
from typing import TypedDict

__all__ = (
    "ExternalSourceData",
)

class ExternalSourceData(TypedDict):
    name: str
    url: str