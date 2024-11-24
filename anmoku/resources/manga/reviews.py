from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

    from ...typing.jikan import (
        ReviewData,
        JikanResponseData,
    )

from dataclasses import dataclass, field

from ..base import JikanResource
from ..helpers import Review

__all__ = (
    "MangaReviews",
)

@dataclass
class MangaReviews(JikanResource):
    _get_endpoint = "/manga/{id}/reviews"

    data: JikanResponseData[List[ReviewData]] = field(repr = False)
    
    def __iter__(self):
        for review in self.data["data"]:
            yield Review(review)