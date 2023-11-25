from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional, List

    from ...typing.jikan import (
        AnimeData, 
        FullAnimeData, 
        JikanResponseData,
    )

from dataclasses import dataclass, field

from ..base import JikanResource

from ..title import Title
from ..image import Image

__all__ = (
    "Anime", 
    "FullAnime"
)

@dataclass
class Anime(JikanResource):
    _get_endpoint = "/anime/{id}"

    data: JikanResponseData[AnimeData] = field(repr=False)

    id: int = field(init = False)
    """The MyAnimeList ID of the anime."""
    title: Title = field(init = False)
    """The anime's title."""
    url: str = field(init = False)
    """The MyAnimeList URL of the anime."""
    image: Image = field(init = False)
    """The banner image of the anime."""
    # TODO: trailer
    approved: bool = field(init = False)
    """Whether the entry is pending approval on MAL or not."""
    # TODO: titles, type (will be an enum)
    source: Optional[str] = field(init = False)
    """The original material/source the anime was adapted from."""

    def __post_init__(self):
        anime = self.data["data"]

        self.id = anime["mal_id"]
        self.title = Title(anime["titles"])
        self.url = anime["url"]
        self.image = Image(anime["images"])
        self.approved = anime["approved"]
        self.source = anime.get("source")

@dataclass
class FullAnime(Anime):
    _get_endpoint = "/anime/{id}/full"

    data: JikanResponseData[FullAnimeData]