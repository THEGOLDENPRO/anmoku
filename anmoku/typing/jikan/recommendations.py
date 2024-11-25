from __future__ import annotations
from typing import TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from .image import ImageData

__all__ = (
    "RecommendationsData",
)

class EntryData(TypedDict):
    mal_id: int
    url: str
    images: ImageData
    title: str

class RecommendationsData(TypedDict):
    entry: EntryData