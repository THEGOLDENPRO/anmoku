from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...typing.jikan import RecommendationsData

from dataclasses import dataclass, field

from .image import Image

__all__ = ("Recommendation",)

@dataclass
class Recommendation():
    data: RecommendationsData = field(repr = False)

    id: int = field(init = False)
    """The MyAnimeList ID of the recommendation."""
    url: str = field(init = False)
    """The MyAnimeList URL of the recommendation."""
    images: Image = field(init = False)
    """The banner image of the recommendation."""
    title: str = field(init = False)
    """The title of the recommendation."""
    name: str = field(init = False)
    """Alias to `Recommendation.title`"""

    def __post_init__(self):
        item = self.data["entry"]

        self.id = item["mal_id"]
        self.url = item["url"]
        self.images = Image(item["images"])
        self.title = item["title"]
        self.name = self.title