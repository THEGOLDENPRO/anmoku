from __future__ import annotations
from datetime import datetime
from typing import TYPE_CHECKING

if TYPE_CHECKING:

    from ...typing.jikan import (
        NewsData, 
    )

from dataclasses import dataclass, field

from .image import Image
from .author import Author

__all__ = (
    "News",
)

@dataclass
class News():
    data: NewsData = field(repr = False)

    id: int = field(init = False)
    """The MyAnimeList ID for this news article."""
    url: str = field(init = False)
    """The MyAnimeList URL for this news article."""
    title: str = field(init = False)
    """The title of the news article."""
    name: str = field(init = False)
    """Alias to ``News.title``."""
    date: datetime = field(init = False)
    """The publication date of this news article."""
    author: Author = field(init = False)
    """The author who wrote this news article."""
    forum_url: str = field(init = False)
    """The URL to the news article's forum post."""
    image: Image = field(init = False)
    """The banner image of this news article."""
    comments: int = field(init = False)
    """The amount of comments on this news article."""
    excerpt: str = field(init = False)
    """A brief preview of the news article content."""

    def __post_init__(self):
        news = self.data
        
        self.id = news["mal_id"]
        self.url = news["url"]
        self.title = news["title"]
        self.name = self.title
        self.date = datetime.fromisoformat(news["date"])
        self.author = Author(
            url = news["author_url"],
            username = news["author_username"]
        )
        self.forum_url = news["forum_url"]
        self.image = Image(news["images"])
        self.comments = news["comments"]
        self.excerpt = news["excerpt"]