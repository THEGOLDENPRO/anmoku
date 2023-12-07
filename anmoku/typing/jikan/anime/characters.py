from __future__ import annotations
from typing import TypedDict, final, List
from ..character import PartialCharacterData
from ..person import PartialPersonData

__all__ = (
    "AnimeCharacterData",
)

@final
class VoiceActorData(TypedDict):
    person: PartialPersonData
    language: str

@final
class AnimeCharacterData(TypedDict):
    character: PartialCharacterData
    role: str
    voice_actors: List[VoiceActorData]
    favorites: int