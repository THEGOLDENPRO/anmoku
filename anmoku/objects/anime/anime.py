from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional

    from ...typing.jikan import (
        AnimeData, 
        FullAnimeData, 
        JikanResponseData,
    )

from dataclasses import dataclass, field

from ..base import JikanObject
from ..image import Image

__all__ = (
    "Anime", 
    "FullAnime"
)

@dataclass
class Anime(JikanObject):
    _get_endpoint = "/anime/{id}"

    data: JikanResponseData[AnimeData]

    id: int = field(init = False)
    url: str = field(init = False)
    image: Image = field(init = False)
    # TODO: trailer
    approved: bool = field(init = False)
    # TODO: titles, type (will be an enum)
    source: Optional[str] = field(init = False)

    def __post_init__(self):
        anime = self.data["data"]

        self.id = anime["mal_id"]
        self.url = anime["url"]
        self.image = Image(anime["images"])
        self.approved = anime["approved"]
        self.source = anime["source"]

@dataclass
class FullAnime(Anime):
    _get_endpoint = "/anime/{id}/full"

    data: JikanResponseData[FullAnimeData]