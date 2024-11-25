from __future__ import annotations
from typing import Optional, TypedDict

__all__ = (
    "ForumData", 
    "LastCommentData",
)

class LastCommentData(TypedDict):
    url: str
    author_username: str
    author_url: str
    date: str

class ForumData(TypedDict):
    mal_id: int
    url: str
    title: str
    date: str
    author_username: str
    author_url: str
    comments: int
    last_comment: Optional[LastCommentData]