from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Generator, Any

    from ...typing.jikan import (
        RelationData,
        JikanResponseData,
    )

from dataclasses import dataclass

from ..base import JikanIterableResource
from ..helpers import Relation

__all__ = (
    "AnimeRelations",
)

@dataclass
class AnimeRelations(JikanIterableResource):
    _get_endpoint = "/anime/{id}/relations"

    data: JikanResponseData[List[RelationData]]
    
    def __post_init__(self):
        super().__post_init__(Relation)

    def __next__(self) -> Relation:
        return super().__next__()

    def __iter__(self) -> Generator[Relation, Any, None]:
        return super().__iter__()