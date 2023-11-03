from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, final

if TYPE_CHECKING:
    from typing import List, Literal, Any

__all__ = (
    "AnimeData",
    "FullAnimeData"
)

# NOTE: This module is subject to change. I may move some types here to a central location to be used in other types.

class _ImageData(TypedDict):
    image_url: str
    small_image_url: str
    large_image_url: str

@final
class ImagesData(TypedDict):
    jpg: _ImageData
    webp: _ImageData

@final
class TrailerData(TypedDict):
    youtube_id: str
    url: str
    embed_url: str

@final
class TitleData(TypedDict):
    type: Literal["Default", "Synonym", "Japanese", "English"]
    title: str

class _AiredDateData(TypedDict):
    day: int
    month: int
    year: int

class _FromToDateData(TypedDict):
    _from: _AiredDateData # TODO: This also needs to be "from"!
    to: _AiredDateData

@final
class AiredData(TypedDict):
    _from: str # TODO: This needs to be "from" but I can't use from as it's an inbuilt keyword, help!
    to: str
    prop: _FromToDateData

@final
class BroadcastData(TypedDict):
    day: str
    time: str
    timezone: str
    string: str

class _ExtraInfoPointersData(TypedDict): # TODO: I will change this later, just doing this now for the sake of convenience.
    mal_id: int
    type: str
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
    type: Literal["TV", "Movie", "ONA"] | Any[str] # TODO: Find the rest of these.
    source: str
    episodes: int
    status: Literal["Not yet aired", "Currently Airing", "Finished Airing"]
    airing: bool
    aired: AiredData
    duration: str
    rating: Literal["G - All Ages", "PG-13 - Teens 13 or older"] | Any[str] # TODO: Find the rest of these.
    score: int
    score_by: int
    rank: int
    popularity: int
    members: int
    favorites: int
    synopsis: str
    background: int
    season: Literal["summer", "fall"] | Any[str] # TODO: Find the rest of these then remove Any.
    year: int
    broadcast: BroadcastData
    producers: List[_ExtraInfoPointersData]
    licensors: List[_ExtraInfoPointersData]
    studios: List[_ExtraInfoPointersData]
    genres: List[_ExtraInfoPointersData]
    explicit_genres: List[_ExtraInfoPointersData]
    themes: List[_ExtraInfoPointersData]
    demographics: List[_ExtraInfoPointersData]

@final
class FullAnimeData(AnimeData): # TODO: Finish this.
    ...