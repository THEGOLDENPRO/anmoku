from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

    from ...typing.jikan import (
        RelationData,
        JikanResponseData,
    )

from dataclasses import dataclass, field

from ..base import JikanResource
from ..helpers import Relation

__all__ = (
    "MangaRelations",
)

@dataclass
class MangaRelations(JikanResource):
    _get_endpoint = "/manga/{id}/relations"

    data: JikanResponseData[List[RelationData]] = field(repr = False)
    
    def __iter__(self):
        for relation in self.data["data"]:
            yield Relation(relation)