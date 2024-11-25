from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

    from ...typing.jikan import (
        GenreData,
        JikanResponseData,
    )

from dataclasses import dataclass, field

from ..base import JikanResource
from ..helpers import Genre

__all__ = (
    "AnimeGenres",
)

@dataclass
class AnimeGenres(JikanResource):
    _genres_endpoint = "/genres/anime"

    data: JikanResponseData[List[GenreData]] = field(repr = False)
    
    def __iter__(self):
        for genre in self.data["data"]:
            yield Genre(genre)