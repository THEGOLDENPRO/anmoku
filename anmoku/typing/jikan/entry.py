from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from typing import List

__all__ = (
    "EntryData",
    "RelationData",
)

class EntryData(TypedDict):
    mal_id: int
    type: str
    name: str
    url: str

class RelationData(TypedDict):
    relation: str
    entry: List[EntryData]