from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:

    from ...typing.jikan import (
        ForumData,
        LastCommentData
    )

from dataclasses import dataclass, field

__all__ = (
    "Forum",
)

@dataclass
class LastComment():
    data: LastCommentData = field(repr = False)

    url: str = field(init = False)
    """The MyAnimeList URL for this comment."""
    author_username: str = field(init = False)
    """The username of the author who wrote this forum article."""
    author_url: str = field(init = False)
    """The profile URL of the author on MyAnimeList."""
    date: datetime = field(init = False)
    """The date when this was commented."""

    def __post_init__(self):
        comment = self.data
        
        self.url = comment["url"]
        self.author_username = comment["author_username"]
        self.author_url = comment["author_url"]
        self.date = datetime.fromisoformat(comment["date"])

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
    author_username: str = field(init = False)
    """The username of the author who wrote this forum article."""
    author_url: str = field(init = False)
    """The profile URL of the author on MyAnimeList."""
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
        self.author_username = forum["author_username"]
        self.author_url = forum["author_url"]
        self.comments = forum["comments"]

        last_comment = forum["last_comment"]

        if last_comment is not None:
            self.last_comment = LastComment(last_comment)