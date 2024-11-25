from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...typing.jikan import (
        GenreData,
    )

from dataclasses import dataclass, field

__all__ = (
    "Genre",
)

@dataclass
class Genre():
    data: GenreData = field(repr = False)

    id: int = field(init = False)
    name: str = field(init = False)
    url: str = field(init = False)
    count: int = field(init = False)

    def __post_init__(self):
        genre = self.data

        self.id = genre["mal_id"]
        self.name = genre["name"]
        self.url = genre["url"]
        self.count = genre["count"]