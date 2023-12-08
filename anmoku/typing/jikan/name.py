from __future__ import annotations
from typing import TypedDict, Optional

__all__ = (
    "NameData",
)

class NameData(TypedDict):
    name: str
    name_kanji: Optional[str]