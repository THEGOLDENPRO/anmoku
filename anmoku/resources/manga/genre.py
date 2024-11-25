from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Generator, Any

    from ...typing.jikan import (
        GenreData,
        JikanResponseData,
    )

from dataclasses import dataclass

from ..base import JikanIterableResource
from ..helpers import Genre

__all__ = (
    "MangaGenres",
)

@dataclass
class MangaGenres(JikanIterableResource):
    _get_endpoint = "/genres/manga"

    data: JikanResponseData[List[GenreData]]

    def __post_init__(self):
        super().__post_init__(Genre)

    def __next__(self) -> Genre:
        return super().__next__()

    def __iter__(self) -> Generator[Genre, Any, None]:
        return super().__iter__()