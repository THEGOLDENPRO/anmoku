from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

    from ...typing.jikan.review import UserData, ReactionsData
    from ...typing.jikan import ReviewData

from dataclasses import dataclass, field
from datetime import datetime

from .image import Image

__all__ = ("Review",)

@dataclass
class User():
    data: UserData = field(repr = False)

    username: str = field(init = False)
    """The MyAnimeList Username of the reviewer."""
    url: str = field(init = False)
    """The MyAnimeList Profile URL of the reviewer."""
    image: Image = field(init = False)
    """The Profile Picture of the reviewer."""

    def __post_init__(self):
        user = self.data

        self.username = user["username"]
        self.url = user["url"]
        self.image = Image(user["images"])

@dataclass
class Reactions():
    data: ReactionsData = field(repr = False)

    overall: int = field(init = False)
    nice: int = field(init = False)
    love_it: int = field(init = False)
    funny: int = field(init = False)
    confusing: int = field(init = False)
    informative: int = field(init = False)
    well_written: int = field(init = False)
    creative: int = field(init = False)

    def __post_init__(self):
        reactions = self.data

        self.overall = reactions["overall"]
        self.nice = reactions["nice"]
        self.love_it = reactions["love_it"]
        self.funny = reactions["funny"]
        self.confusing = reactions["confusing"]
        self.informative = reactions["informative"]
        self.well_written = reactions["well_written"]
        self.creative = reactions["creative"]

@dataclass
class Review():
    data: ReviewData = field(repr = False)

    user: User = field(init = False)
    """The user reviewing this."""
    url: str = field(init = False)
    """The MyAnimeList URL of the review."""
    reactions: Reactions = field(init = False)
    """Reactions to this review."""
    date: datetime = field(init = False)
    """The date when this review was posted."""
    review: str = field(init = False)
    """The review content."""
    content: str = field(init = False)
    """Alias for `Review.review`"""
    score: int = field(init = False)
    """The score on the review."""
    tags: List[str] = field(init = False)
    """The tags on the Review."""
    spoiler: bool = field(init = False)
    """Review contains spoiler."""
    preliminary: bool = field(init = False)

    def __post_init__(self):
        review = self.data

        self.user = User(review["user"])
        self.url = review["url"]
        self.reactions = Reactions(review["reactions"])
        self.date = datetime.fromisoformat(review["date"])
        self.review = review["review"]
        self.content = self.review
        self.score = review["score"]
        self.tags = review["tags"]
        self.spoiler = review["is_spoiler"]
        self.preliminary = review["is_preliminary"]