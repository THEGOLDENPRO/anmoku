from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from ..typing.jikan import (
        AnimeData, 
        FullAnimeData, 
        AnimeCharacterData, 
        JikanResponseData, 

        # Temporary
        # -----------
        PartialPerson,
        PartialCharacter
    )

    from ..typing.jikan.anime import VoiceActorData

from dataclasses import dataclass, field

__all__ = (
    "Anime", 
    "FullAnime",
    "AnimeCharacters"
)

@dataclass
class Anime():
    _get_endpoint = "/anime/{id}"

    data: JikanResponseData[AnimeData]

@dataclass
class FullAnime(Anime):
    _get_endpoint = "/anime/{id}/full"

    data: JikanResponseData[FullAnimeData]


@dataclass
class VoiceActor():
    data: VoiceActorData

    person: PartialPerson = field(init = False) # TODO: Change this to actual person class.
    language: str = field(init = False)

    def __post_init__(self):
        self.person = self.data.get("person")
        self.language = self.data.get("language")

@dataclass
class AnimeCharacter():
    data: AnimeCharacterData

    character: PartialCharacter = field(init = False) # TODO: Change this to actual character class.
    role: str = field(init = False)
    voice_actors: List[VoiceActor] = field(init = False)

    def __post_init__(self):
        self.character = self.data.get("character")
        self.role = self.data.get("role")
        self.voice_actors = [VoiceActor(actor) for actor in self.data.get("voice_actors", [])]

@dataclass
class AnimeCharacters():
    _get_endpoint = "/anime/{id}/characters"

    data: JikanResponseData[List[AnimeCharacterData]]

    def __iter__(self):

        for character in self.data["data"]:
            yield AnimeCharacter(character)