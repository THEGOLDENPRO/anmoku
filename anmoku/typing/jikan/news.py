from __future__ import annotations
from typing import TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from .image import ImagesData

__all__ = ("NewsData",)

class NewsData(TypedDict):
    mal_id: int
    url: str
    title: str
    date: str
    author_username: str
    author_url: str
    forum_url: str
    images: ImagesData
    comments: int
    excerpt: str