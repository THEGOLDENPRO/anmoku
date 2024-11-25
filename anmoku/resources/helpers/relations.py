from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

    from ...typing.jikan import (
        RelationData,
        EntryData,
    )

from dataclasses import dataclass, field

__all__ = (
    "Entry",
    "Relation",
)

@dataclass
class Entry():
    data: EntryData = field(repr = False)

    id: int = field(init = False)
    type: str = field(init = False)
    name: str = field(init = False)
    url: str = field(init = False)

    def __post_init__(self):
        entry = self.data

        self.id = entry["mal_id"]
        self.type = entry["type"]
        self.name = entry["name"]
        self.url = entry["url"]

@dataclass
class Relation():
    data: RelationData = field(repr = False)

    relation: str = field(init = False)

    entries: List[Entry] = field(init = False)

    def __post_init__(self):
        self.relation = self.data["relation"]
        
        entries = self.data["entry"]

        self.entries = [Entry(entry) for entry in entries]