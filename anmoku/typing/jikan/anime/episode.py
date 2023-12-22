from __future__ import annotations
from typing import TypedDict, final, Optional

__all__ = (
    "AnimeEpisodeData",
)

@final
class AnimeEpisodeData(TypedDict):
    mal_id: int
    url: Optional[str]
    title: str
    title_japanese: str
    title_romanji: str
    # duration: Optional[int] # this just doesn't exist lmao
    aired: Optional[str]
    filler: bool
    recap: bool
    forum_url: Optional[str]