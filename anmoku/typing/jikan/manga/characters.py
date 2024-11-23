from __future__ import annotations
from typing import TypedDict, final

from ..character import PartialCharacterData

__all__ = (
    "MangaCharacterData",
)

@final
class MangaCharacterData(TypedDict):
    character: PartialCharacterData
    role: str