from __future__ import annotations
from typing import TypedDict, final, Optional

__all__ = (
    "AnimeEpisodeData",
    "SingleAnimeEpisodeData"
)

@final
class AnimeEpisodeData(TypedDict):
    mal_id: int
    url: Optional[str]
    title: str
    title_japanese: Optional[str]
    title_romanji: Optional[str]
    score: Optional[float]
    aired: Optional[str]
    filler: bool
    recap: bool
    forum_url: Optional[str]

@final
class SingleAnimeEpisodeData(TypedDict):
    mal_id: int
    url: str
    title: str
    title_japanese: Optional[str]
    title_romanji: Optional[str]
    duration: Optional[int]
    aired: Optional[str]
    filler: bool
    recap: bool
    synopsis: Optional[str]