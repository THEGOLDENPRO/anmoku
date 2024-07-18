from __future__ import annotations
from typing import (
    TypedDict, final, 
    List, Literal, Any, Optional
)
from ...mal import MALRatings
from ..datetime import DateRangeData
from ..title import TitleData

__all__ = (
    "AnimeData",
    "FullAnimeData",
    "PartialAnimeData",
)

# NOTE: This module is subject to change. I may move some types here to a central location to be used in other types.

AnimeTypesData = Literal["TV", "Movie", "ONA", "OVA", "Special", "Music"]
AnimeAiringStatusData = Literal["Not yet aired", "Currently Airing", "Finished Airing"]

class ImageData(TypedDict):
    image_url: str
    small_image_url: str
    large_image_url: str

@final
class ImagesData(TypedDict):
    jpg: ImageData
    webp: ImageData

@final
class TrailerImageData(ImageData):
    medium_image_url: str
    maximum_image_url: str

@final
class TrailerData(TypedDict):
    youtube_id: str
    url: str
    embed_url: str
    images: TrailerImageData

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


class PartialAnimeData(TypedDict):
    mal_id: int
    url: str
    images: ImagesData
    title: str

class AnimeData(PartialAnimeData): # TODO: Redo these types but this time following the response scheme. https://docs.api.jikan.moe/#tag/anime/operation/getAnimeById
    trailer: TrailerData
    approved: bool
    titles: List[TitleData]
    title_english: str
    title_japanese: str
    title_synonyms: List[str]
    type: Optional[AnimeTypesData]
    source: Optional[str]
    episodes: Optional[int]
    status: AnimeAiringStatusData
    airing: bool
    aired: DateRangeData
    duration: str
    rating: MALRatings
    score: Optional[int]
    score_by: Optional[int]
    rank: Optional[int]
    popularity: Optional[int]
    members: Optional[int]
    favorites: Optional[int]
    synopsis: Optional[str]
    background: Optional[int]
    season: Literal["summer", "fall"] | Any # TODO: Find the rest of these then remove Any.
    year: Optional[int]
    broadcast: BroadcastData
    producers: List[EntryData]
    licensors: List[EntryData]
    studios: List[EntryData]
    genres: List[EntryData]
    explicit_genres: List[EntryData]
    themes: List[EntryData]
    demographics: List[EntryData]

@final
class FullAnimeData(AnimeData):
    relations: List[RelationData]
    theme: ThemeData
    external: List[ExternalSourceData]
    streaming: List[ExternalSourceData]