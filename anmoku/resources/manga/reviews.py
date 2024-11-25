from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Generator, Any

    from ...typing.jikan import (
        ReviewData,
        JikanResponseData,
    )

from dataclasses import dataclass

from ..base import JikanIterableResource
from ..helpers import Review

__all__ = (
    "MangaReviews",
)

@dataclass
class MangaReviews(JikanIterableResource):
    _get_endpoint = "/manga/{id}/reviews"

    data: JikanResponseData[List[ReviewData]]
    
    def __post_init__(self):
        super().__post_init__(Review)

    def __next__(self) -> Review:
        return super().__next__()

    def __iter__(self) -> Generator[Review, Any, None]:
        return super().__iter__()