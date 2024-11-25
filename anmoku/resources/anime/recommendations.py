from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Generator, Any

    from ...typing.jikan import (
        RecommendationsData,
        JikanResponseData,
    )

from dataclasses import dataclass

from ..base import JikanIterableResource
from ..helpers import Recommendation

__all__ = (
    "AnimeRecommendations",
)

@dataclass
class AnimeRecommendations(JikanIterableResource):
    _get_endpoint = "/anime/{id}/recommendations"

    data: JikanResponseData[List[RecommendationsData]]
    
    def __post_init__(self):
        super().__post_init__(Recommendation)

    def __next__(self) -> Recommendation:
        return super().__next__()

    def __iter__(self) -> Generator[Recommendation, Any, None]:
        return super().__iter__()