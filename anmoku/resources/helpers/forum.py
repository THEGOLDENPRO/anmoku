from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:

    from ...typing.jikan import (
        ForumData,
        LastCommentData
    )

from dataclasses import dataclass, field

from .author import Author

__all__ = (
    "Forum",
)

@dataclass
class Forum():
    data: ForumData = field(repr = False)

    id: int = field(init = False)
    """The MyAnimeList ID for this forum article."""
    url: str = field(init = False)
    """The MyAnimeList URL for this forum article."""
    title: str = field(init = False)
    """The title of the forum article."""
    name: str = field(init = False)
    """Alias to ``Forum.title``."""
    date: datetime = field(init = False)
    """The publication date of this forum article."""
    author: Author = field(init = False)
    """The author who wrote this forum article."""
    comments: int = field(init = False)
    """The amount of comments on this forum article."""
    last_comment: LastComment = field(init = False, default = None)
    """Last comment on that forum article."""

    def __post_init__(self):
        forum = self.data
        
        self.id = forum["mal_id"]
        self.url = forum["url"]
        self.title = forum["title"]
        self.name = self.title
        self.date = datetime.fromisoformat(forum["date"])
        self.author = Author(
            url = forum["author_url"],
            username = forum["author_username"]
        )
        self.comments = forum["comments"]

        last_comment = forum["last_comment"]

        if last_comment is not None:
            self.last_comment = LastComment(last_comment)

@dataclass
class LastComment():
    data: LastCommentData = field(repr = False)

    url: str = field(init = False)
    """The MyAnimeList URL for this comment."""
    author: Author = field(init = False)
    """The author who wrote this forum article."""
    date: datetime = field(init = False)
    """The date when this was commented."""

    def __post_init__(self):
        comment = self.data

        self.url = comment["url"]
        self.author = Author(
            url = comment["author_url"],
            username = comment["author_username"]
        )
        self.date = datetime.fromisoformat(comment["date"])