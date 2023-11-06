from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, final

if TYPE_CHECKING:
    from typing import List, TypeVar
    from typing_extensions import NotRequired

    from .anime import PartialAnimeData
    from .person import PartialPersonData

    T = TypeVar("T")

__all__ = (
    "CharacterData",
    "FullCharacterData",
    "PartialCharacterData"
)

class CharacterImageData(TypedDict):
    image_url: str
    small_image_url: NotRequired[str] # Doesn't always exist. 😑

class CharacterImagesData(TypedDict):
    jpg: CharacterImageData
    webp: CharacterImageData

class CharacterAnimeData(TypedDict):
    role: str
    anime: PartialAnimeData

class CharacterMangaData(TypedDict):
    role: str
    manga: PartialAnimeData # Anime, manga same thing lmao. # TODO: We should change this once we have MangaData though.

class CharacterVoicesData(TypedDict):
    language: str
    person: PartialPersonData


class PartialCharacterData(TypedDict):
    mal_id: int
    url: str
    images: CharacterImagesData
    name: str

class CharacterData(PartialCharacterData):
    name_kanji: NotRequired[str]
    nicknames: List[str]
    favorites: int
    about: NotRequired[str]

@final
class FullCharacterData(CharacterData):
    anime: List[CharacterAnimeData]
    manga: List[CharacterMangaData]
    voices: List[CharacterVoicesData]