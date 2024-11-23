from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from ...typing.jikan.manga.characters import MangaCharacterData
    from ...typing.jikan.api import JikanResponseData

from dataclasses import dataclass, field

from ..base import JikanResource
from ..helpers.image import Image

__all__ = (
    "MangaCharacters",
)


@dataclass
class MangaCharacter():
    data: MangaCharacterData = field(repr = False)

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

    def __post_init__(self):
        character = self.data["character"]

        self.id = character["mal_id"]
        self.name = character["name"]
        self.url = character["url"]
        self.image = Image(character["images"])

        self.role = self.data["role"]

@dataclass
class MangaCharacters(JikanResource):
    """Get data of the characters from a particular manga."""
    _get_endpoint = "/manga/{id}/characters"

    data: JikanResponseData[List[MangaCharacterData]]

    def __iter__(self):

        for character in self.data["data"]:
            yield MangaCharacter(character)