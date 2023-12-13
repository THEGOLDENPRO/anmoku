from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from ...typing.jikan import (
        AnimeCharacterData, 
        JikanResponseData
    )

    from ...typing.jikan.anime.characters import VoiceActorData

from dataclasses import dataclass, field

from ..helpers import Image
from ..base import JikanResource

__all__ = (
    "AnimeCharacters",
)

@dataclass
class VoiceActor():
    data: VoiceActorData

    id: int = field(init = False)
    """The MyAnimeList ID of this voice actor."""
    url: str = field(init = False)
    """The MyAnimeList URL to this voice actor."""
    name: str = field(init = False)
    """The name of this voice actor."""
    image: Image = field(init = False)
    """The image of this voice actor."""

    language: str = field(init = False)
    """The language they are voice acting in."""

    def __post_init__(self):
        person = self.data["person"]

        self.id = person["mal_id"]
        self.url = person["url"]
        self.name = person["name"]
        self.image = Image(person["images"])
        self.language = self.data["language"]

@dataclass
class AnimeCharacter():
    data: AnimeCharacterData

    id: int = field(init = False)
    """The MyAnimeList ID of this character."""
    name: str = field(init = False)
    """The name of this character."""
    url: str = field(init = False)
    """The MyAnimeList URL to this character."""
    image: Image = field(init = False)
    """The image of this character."""

    role: str = field(init = False)
    """The character's role."""
    voice_actors: List[VoiceActor] = field(init = False)
    """The list of voice actors who acted this character."""

    def __post_init__(self):
        character = self.data["character"]

        self.id = character["mal_id"]
        self.name = character["name"]
        self.url = character["url"]
        self.image = Image(character["images"])

        self.role = self.data["role"]
        self.voice_actors = [VoiceActor(actor) for actor in self.data.get("voice_actors", [])]

@dataclass
class AnimeCharacters(JikanResource):
    """Get data of the characters from a particular anime."""
    _get_endpoint = "/anime/{id}/characters"

    data: JikanResponseData[List[AnimeCharacterData]]

    def __iter__(self):

        for character in self.data["data"]:
            yield AnimeCharacter(character)