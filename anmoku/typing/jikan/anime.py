from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, final

if TYPE_CHECKING:
    from typing import List, Literal, Any
    from .character import PartialCharacter
    from .person import PartialPerson
    from ..mal import MALRatings

__all__ = (
    "AnimeData",
    "FullAnimeData",
    "AnimeCharacterData"
)

# NOTE: This module is subject to change. I may move some types here to a central location to be used in other types.

class ImageData(TypedDict):
    image_url: str
    small_image_url: str
    large_image_url: str

@final
class ImagesData(TypedDict):
    jpg: ImageData
    webp: ImageData

@final
class TrailerData(TypedDict):
    youtube_id: str
    url: str
    embed_url: str

@final
class TitleData(TypedDict):
    type: Literal["Default", "Synonym", "Japanese", "English"]
    title: str

class AiredDateData(TypedDict):
    day: int
    month: int
    year: int

AiredPropData = TypedDict("_AiredPropData", {"from": AiredDateData, "to": AiredDateData})
AiredData = TypedDict("AiredData", {"from": str, "to": str, "prop": AiredPropData})

@final
class BroadcastData(TypedDict):
    day: str
    time: str
    timezone: str
    string: str

class EntryData(TypedDict):
    mal_id: int
    type: str
    name: str
    url: str

class RelationData(TypedDict):
    relation: str
    entry: List[EntryData]

class ThemeData(TypedDict):
    openings: List[str]
    endings: List[str]

class ExternalSourceData(TypedDict):
    name: str
    url: str


class AnimeData(TypedDict):
    mal_id: int
    url: str
    images: ImagesData
    trailer: TrailerData
    approved: bool
    titles: List[TitleData]
    title_english: str
    title_japanese: str
    title_synonyms: List[str]
    type: Literal["TV", "Movie", "ONA", "Special"] # TODO: Find the rest of these.
    source: str
    episodes: int
    status: Literal["Not yet aired", "Currently Airing", "Finished Airing"]
    airing: bool
    aired: AiredData
    duration: str
    rating: MALRatings
    score: int
    score_by: int
    rank: int
    popularity: int
    members: int
    favorites: int
    synopsis: str
    background: int
    season: Literal["summer", "fall"] | Any # TODO: Find the rest of these then remove Any.
    year: int
    broadcast: BroadcastData
    producers: List[EntryData]
    licensors: List[EntryData]
    studios: List[EntryData]
    genres: List[EntryData]
    explicit_genres: List[EntryData]
    themes: List[EntryData]
    demographics: List[EntryData]

@final
class FullAnimeData(AnimeData): # TODO: Finish this.
    relations: List[RelationData]
    theme: ThemeData
    external: List[ExternalSourceData]
    streaming: List[ExternalSourceData]


@final
class VoiceActorData(TypedDict):
    person: PartialPerson
    language: str


@final
class AnimeCharacterData(TypedDict):
    character: PartialCharacter
    role: str
    voice_actors: List[VoiceActorData]