from __future__ import annotations
from typing import List, Literal, Optional, TypedDict

from ..datetime import DateRangeData
from ..title import TitleData
from ..image import ImagesData

__all__ = (
    "MangaData",
    "FullMangaData",
    "PartialMangaData",
    "MoreInfoMangaData"
)

MangaStatus = Literal["Publishing", "Finished", "Discontinued"]

class EntryData(TypedDict):
    mal_id: int
    type: str
    name: str
    url: str

class RelationData(TypedDict):
    relation: str
    entry: List[EntryData]

class ExternalSourceData(TypedDict):
    name: str
    url: str

class PartialMangaData(TypedDict):
    mal_id: int
    url: str
    images: ImagesData
    title: str

class MangaData(PartialMangaData):
    approved: bool
    titles: List[TitleData]
    title_english: str
    title_japanese: str
    title_synonyms: List[str]
    type: str
    chapters: int
    volumes: int
    status: MangaStatus
    publishing: bool
    published: DateRangeData
    score: Optional[int]
    score_by: Optional[int]
    rank: Optional[int]
    popularity: Optional[int]
    members: Optional[int]
    favorites: Optional[int]
    synopsis: Optional[str]
    background: Optional[str]
    authors: List[EntryData]
    serializations: List[EntryData]
    genres: List[EntryData]
    explicit_genres: List[EntryData]
    themes: List[EntryData]
    demographics: List[EntryData]

class FullMangaData(MangaData):
    title_synonyms: List[str]
    relations: RelationData
    external: List[ExternalSourceData]

class MoreInfoMangaData(TypedDict):
    moreinfo: str