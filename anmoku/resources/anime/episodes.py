from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Optional
    from ...typing.jikan import (
        AnimeEpisodeData, 
        JikanPageResponseData
    )
    from ...typing.jikan.title import TitleData

from datetime import datetime
from dataclasses import dataclass, field

from ..helpers import Title
from ..base import JikanResource

__all__ = (
    "AnimeEpisodes",
)

@dataclass
class AnimeEpisode():
    data: AnimeEpisodeData = field(repr = False)

    id: int = field(init = False)
    """The MyAnimeList ID of this episode."""
    title: Title = field(init = False)
    """The title of this episode."""
    name: Title = field(init = False)
    """Alias to ``AnimeEpisode.title``."""
    url: Optional[str] = field(init = False)
    """The MyAnimeList URL to this episode."""
    aired: Optional[datetime] = field(init = False, default = None)
    """The date this episode was aired."""
    filler: bool = field(init = False)
    """Is this episode a filler episode or not."""
    recap: bool = field(init = False)
    """Is this episode a recap episode or not."""
    forum_url: Optional[str] = field(init = False)
    """The URL to the forum discussion of this episode."""

    def __post_init__(self):
        self.id = self.data["mal_id"]

        titles: List[TitleData] = []

        japanese_title = self.data["title_japanese"]
        if japanese_title is not None:
            titles.append(
                {"type": "Japanese", "title": japanese_title}
            )

        romanji_title = self.data["title_romanji"]
        if romanji_title is not None:
            titles.append(
                {"type": "Japanese", "title": romanji_title}
            )

        titles.append(
            {"type": "Default", "title": self.data["title"]}
        )

        self.title = Title(titles)
        self.name = self.title

        self.url = self.data["url"]

        aired = self.data["aired"]
        if aired is not None:
            self.aired = datetime.fromisoformat(aired)

        self.filler = self.data["filler"]
        self.recap = self.data["recap"]
        self.forum_url = self.data["forum_url"]

@dataclass
class AnimeEpisodes(JikanResource):
    """Get an anime's episodes."""
    _get_endpoint = "/anime/{id}/episodes"

    data: JikanPageResponseData[List[AnimeEpisodeData]]

    def __iter__(self):

        for episode in self.data["data"]:
            yield AnimeEpisode(episode)