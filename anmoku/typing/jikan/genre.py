from __future__ import annotations
from typing import TypedDict

__all__ = (
    "GenreData",
)

class GenreData(TypedDict):
    mal_id: int
    name: str
    url: str
    count: int