from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Optional, Generator, Any
    from ...typing.jikan import (
        AnimeEpisodeData,
        SingleAnimeEpisodeData,
        JikanResponseData,
        JikanPageResponseData
    )

from datetime import datetime, timedelta
from dataclasses import dataclass, field

from ..helpers import Title
from ..base import JikanResource, JikanIterableResource

__all__ = (
    "AnimeEpisodes",
    "SingleAnimeEpisode"
)

@dataclass
class AnimeEpisodes(JikanIterableResource):
    """Get an anime's episodes with anime's ID."""
    _get_endpoint = "/anime/{id}/episodes"

    data: JikanPageResponseData[List[AnimeEpisodeData]]

    def __post_init__(self):
        super().__post_init__(AnimeEpisode)

    def __next__(self) -> AnimeEpisode:
        return super().__next__()

    def __iter__(self) -> Generator[AnimeEpisode, Any, None]:
        return super().__iter__()

@dataclass
class SingleAnimeEpisode(JikanResource):
    """
    Get's the exact anime episode specified with the ID of the anime and the episode number.

    Required Params
    -----------------
    * `id` - Anime ID
    * `episode` - Episode number

    -------------------

    ⭐ Example
    -----------
    This is how to get an anime episode directly with episode number and anime ID::

        from anmoku import Anmoku, SingleAnimeEpisode

        client = Anmoku()

        # As you can see this request requires an extra argument (episode).
        episode = client.get(SingleAnimeEpisode, id = 1, episode = 2)

        print(f"You requested episode {episode.number}, it's named '{episode.name}' and was released...")
    """
    _get_endpoint = "/anime/{id}/episodes/{episode}"

    data: JikanResponseData[SingleAnimeEpisodeData] = field(repr = False)

    id: int = field(init = False)
    """The MyAnimeList ID of the episode."""
    number: int = field(init = False)
    """The episode number."""
    url: str = field(init = False)
    """The MyAnimeList URL to this episode."""
    title: Title = field(init = False)
    """The title of the anime episode."""
    name: Title = field(init = False)
    """Aliases for title."""
    duration: Optional[timedelta] = field(init = False, default = None)
    """The duration of the episode."""
    aired: Optional[datetime] = field(init = False, default = None)
    """The date this episode was aired."""
    filler: bool = field(init = False)
    """Is the episode a filler episode."""
    recap: bool = field(init = False)
    """Is this episode a recap episode."""
    synopsis: Optional[str] = field(init = False)
    """This episode's synopsis."""

    def __post_init__(self):
        data = self.data["data"]

        self.id = data["mal_id"]
        self.number = self.id
        self.url = data["url"]
        self.title = Title._from_old_title_data(
            default_title = data["title"],
            japanese_title = data["title_japanese"],
            romanji_title = data["title_romanji"]
        )
        self.name = self.title

        duration = data["duration"]

        if duration is not None:
            self.duration = timedelta(seconds = duration)

        aired = data["aired"]

        if aired is not None:
            self.aired = datetime.fromisoformat(aired)

        self.filler = data["filler"]
        self.recap = data["recap"]
        self.synopsis = data["synopsis"]

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

        self.title = Title._from_old_title_data(
            default_title = self.data["title"],
            japanese_title = self.data["title_japanese"],
            romanji_title = self.data["title_romanji"]
        )
        self.name = self.title

        self.url = self.data["url"]

        aired = self.data["aired"]
        if aired is not None:
            self.aired = datetime.fromisoformat(aired)

        self.filler = self.data["filler"]
        self.recap = self.data["recap"]
        self.forum_url = self.data["forum_url"]