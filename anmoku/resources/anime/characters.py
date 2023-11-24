from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from ...typing.jikan import (
        AnimeCharacterData, 
        JikanResponseData, 

        # NOTE: Temporary
        # ----------------
        PartialPersonData,
        PartialCharacterData
    )

    from ...typing.jikan.anime.characters import VoiceActorData

from dataclasses import dataclass, field

from ..image import Image
from ..base import JikanResource

__all__ = (
    "AnimeCharacters",
)

@dataclass
class VoiceActor():
    data: VoiceActorData

    person: PartialPersonData = field(init = False) # TODO: Change this to actual person class.
    language: str = field(init = False)

    def __post_init__(self):
        self.person = self.data.get("person")
        self.language = self.data.get("language")

@dataclass
class AnimeCharacter():
    data: AnimeCharacterData

    partial_character: PartialCharacterData = field(init = False) # TODO: Change this to actual character class.
    role: str = field(init = False)
    voice_actors: List[VoiceActor] = field(init = False)

    id: int = field(init = False)
    name: str = field(init = False)
    url: str = field(init = False)
    image: Image = field(init = False)

    def __post_init__(self):
        character = self.data.get("character")

        self.partial_character = character # TODO: Change this to actual character class.
        self.role = self.data.get("role")
        self.voice_actors = [VoiceActor(actor) for actor in self.data.get("voice_actors", [])]

        self.id = character["mal_id"]
        self.name = character["name"]
        self.url = character["url"]
        self.image = Image(character["images"])

@dataclass
class AnimeCharacters(JikanResource):
    """Get data of the characters from a particular anime."""
    _get_endpoint = "/anime/{id}/characters"

    data: JikanResponseData[List[AnimeCharacterData]]

    def __iter__(self):

        for character in self.data["data"]:
            yield AnimeCharacter(character)