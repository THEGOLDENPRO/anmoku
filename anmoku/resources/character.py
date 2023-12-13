from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Optional
    from ..typing.jikan import (
        JikanResponseData, 
        CharacterData,
        FullCharacterData
    )

from dataclasses import dataclass, field

from .base import JikanResource
from .helpers import Image, Name

__all__ = ("Character", "FullCharacter")

@dataclass
class Character(JikanResource):
    _get_endpoint = "/characters/{id}"
    _search_endpoint = "/characters"

    data: JikanResponseData[CharacterData] = field(repr = False)

    id: int = field(init = False)
    """The MyAnimeList ID of the character."""
    url: str = field(init = False)
    """The MyAnimeList URL to this character."""
    image: Image = field(init = False)
    """The image of this character."""
    name: Name = field(init = False)
    """The name of the character."""
    nicknames: List[str] = field(init = False)
    """List of the character's nicknames."""
    favorites: int = field(init = False)
    """The amount of people who favorited this character."""
    about: Optional[str] = field(init = False, default = None)
    """A description about the character."""

    def __post_init__(self):
        character = self.data["data"]

        self.id = character["mal_id"]
        self.url = character["url"]
        self.image = Image(character["images"])
        self.name = Name(character)
        self.nicknames = character["nicknames"]
        self.favorites = character["favorites"]

        about = character.get("about")

        if about is not None:
            self.about = about

@dataclass
class FullCharacter(Character): # TODO: finish this.
    _get_endpoint = "/characters/{id}/full"

    data: JikanResponseData[FullCharacterData]