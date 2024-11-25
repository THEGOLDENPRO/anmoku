from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional

    from ...typing.jikan.anime.anime import (
        AnimeTypesData,
        AnimeAiringStatusData,
        TrailerData
    )
    from ...typing.jikan import (
        AnimeData, 
        FullAnimeData, 
        JikanResponseData,
        MoreInfoData
    )
    from ...typing.mal import MALRatings

from enum import Enum
from dataclasses import dataclass, field

from ..base import JikanResource
from ..helpers import Title, Image, DateRange

__all__ = (
    "Anime",
    "FullAnime"
)

class AiringStatus(Enum):
    FINISHED = "Finished Airing"
    AIRING = "Currently Airing"
    NOT_YET_AIRED = "Not yet aired"

    def __init__(self, value: AnimeAiringStatusData) -> None:
        ...

class AnimeSeason(Enum):
    SUMMER = "summer"
    WINTER = "winter"
    SPRING = "spring"
    FALL = "fall"

    def __init__(self, value: AnimeAiringStatusData) -> None:
        ...

@dataclass
class Anime(JikanResource):
    """
    Get or search for anime.

    ------------

    ⭐ Example:
    ------------
    Here's an example of how to get an anime by ID and display it's cover art::

        from anmoku import Anime, Anmoku

        client = Anmoku()

        anime = client.get(Anime, id = 13759)

        print(
            f"Got the anime '{anime.name}', it's english name is '{anime.name.english}' and it was aired in {anime.aired.from_.year}."
        )

        # Display it's image.
        anime.image.get_image().show()
    """
    _get_endpoint = "/anime/{id}"
    _search_endpoint = "/anime"
    _random_endpoint = "/random/anime"


    data: JikanResponseData[AnimeData] = field(repr = False)

    id: int = field(init = False)
    """The MyAnimeList ID of the anime."""
    url: str = field(init = False)
    """The MyAnimeList URL to this anime."""
    image: Image = field(init = False)
    """The banner image of the anime."""
    trailer: Trailer = field(init = False)
    """The trailer of the anime."""
    approved: bool = field(init = False)
    """Whether the entry is pending approval on MAL or not."""
    title: Title = field(init = False)
    """The anime's title."""
    name: Title = field(init = False)
    """Alias to ``Anime.title``."""
    type: AnimeTypesData = field(init = False)
    """The type of anime."""
    source: Optional[str] = field(init = False, default = None)
    """The original material / source the anime was adapted from."""
    episodes: int = field(init = False, default = 0)
    """Episode count of the anime."""
    status: AiringStatus = field(init = False, default = AiringStatus.NOT_YET_AIRED)
    """The airing status of the anime."""
    aired: DateRange = field(init = False)
    """To when and from this anime was aired."""
    duration: Optional[str] = field(init = False, default = None)
    """Duration of each episode of an anime or complete duration of an anime film."""
    audience_rating: Optional[MALRatings] = field(init = False, default = None)
    """Audience rating of this anime."""
    score: float = field(init = False, default = 0.0)
    """The anime's score rating."""
    scored_by: int = field(init = False, default = 0)
    """Number of users that scored the anime."""
    rank: int = field(init = False, default = 0)
    popularity: int = field(init = False, default = 0)
    members: int = field(init = False, default = 0)
    favourites: int = field(init = False, default = 0)
    synopsis: Optional[str] = field(init = False, default = None)
    background: Optional[str] = field(init = False, default = None)
    description: Optional[str] = field(init = False, default = None)
    season: Optional[AnimeSeason] = field(init = False, default = None)
    year: int = field(init = False, default = 0)

    def __post_init__(self):
        anime = self.data["data"]

        self.id = anime["mal_id"]
        self.url = anime["url"]
        self.image = Image(anime["images"])
        self.trailer = Trailer(anime["trailer"])
        self.approved = anime["approved"]
        self.title = Title(anime["titles"])
        self.name = self.title
        self.type = anime["type"]
        self.rank = anime["rank"]
        self.popularity = anime["popularity"]
        self.members = anime["members"]
        self.favourites = anime["favorites"]
        self.synopsis = anime["synopsis"]
        self.background = anime["background"]
        self.description = self.synopsis or self.background
        self.source = anime["source"]
        self.duration = anime["duration"]
        self.audience_rating = anime["rating"]

        # "is not None" is used on the keys below to make sure
        # they are undefined so the dataclass fields fall back to their
        # respective default values.
        season = anime["season"]

        if season is not None:
            self.season = AnimeSeason(season)

        episodes = anime["episodes"]

        if episodes is not None:
            self.episodes = episodes

        status = anime["status"]

        if status is not None:
            self.status = AiringStatus(status)

        self.aired = DateRange(anime["aired"])

        score = anime["score"]

        if score is not None:
            self.score = score

        scored_by = anime["scored_by"]

        if scored_by is not None:
            self.scored_by = scored_by

@dataclass
class FullAnime(Anime): # TODO: Finish this. You can use the FullAnimeData type dict to help.
    _get_endpoint = "/anime/{id}/full"

    data: JikanResponseData[FullAnimeData] = field(repr=False)

@dataclass
class AnimeMoreInfo(JikanResource):
    _get_endpoint = "/anime/{id}/moreinfo"

    data: JikanResponseData[MoreInfoData] = field(repr=False)

    more_info: Optional[str] = field(init = False, default = None)

    def __post_init__(self):
        more_info = self.data["data"]["moreinfo"]

        if more_info is not None:
            self.more_info = more_info

@dataclass
class Trailer():
    """Helper for the anime's trailer."""
    data: TrailerData = field(repr = False)

    id: str = field(init = False)
    url: str = field(init = False)
    embed_url: str = field(init = False)
    image: Image = field(init = False)

    def __post_init__(self):
        self.id = self.data["youtube_id"]
        """Video ID of the trailer."""
        self.url = self.data["url"]
        """Url to trailer."""
        self.embed_url = self.data["embed_url"]
        """Url to the trailer's embed."""
        self.image = Image(self.data["images"])
        """Image of the trailer."""