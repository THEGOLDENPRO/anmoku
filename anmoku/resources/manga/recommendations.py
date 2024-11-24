from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...typing.jikan import (
        RecommendationsData,
        JikanResponseData,
    )

from dataclasses import dataclass, field

from ..base import JikanResource
from ..helpers import Recommendation

__all__ = (
    "MangaRecommendations",
)

@dataclass
class MangaRecommendations(JikanResource):
    _get_endpoint = "/manga/{id}/recommendations"

    data: JikanResponseData[RecommendationsData] = field(repr = False)
    
    def __iter__(self):
        for recommendation in self.data["data"]:
            yield Recommendation(recommendation)