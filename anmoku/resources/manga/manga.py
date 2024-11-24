from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from ...typing.jikan.manga.manga import MangaStatus, RelationData, ExternalSourceData
    from ...typing.jikan import (
        MangaData, 
        FullMangaData, 
        JikanResponseData,
    )

from dataclasses import dataclass, field
from enum import Enum

from ..base import JikanResource
from ..helpers import Title, Image, DateRange

__all__ = (
    "Manga", 
    "FullManga"
)


class PublishingStatus(Enum):
    FINISHED = "Finished"
    PUBLISHING = "Publishing"
    DISCONTINUED = "Discontinued"

    def __init__(self, value: MangaStatus) -> None:
        ...

@dataclass
class Manga(JikanResource):
    _get_endpoint = "/manga/{id}"
    _search_endpoint = "/manga"

    data: JikanResponseData[MangaData] = field(repr = False)

    id: int = field(init = False)
    """The MyAnimeList ID of the manga."""
    url: str = field(init = False)
    """The MyAnimeList URL to this manga."""
    image: Image = field(init = False)
    """The banner image of the manga."""
    approved: bool = field(init = False)
    """Whether the entry is pending approval on MAL or not."""
    title: Title = field(init = False)
    """The manga's title."""
    name: Title = field(init = False)
    """Alias to ``Manga.title``."""
    chapters: int = field(init = False, default = 0)
    """Chapter count of the manga."""
    volumes: int = field(init = False, default = 0)
    """Volumes count of the manga."""
    status: PublishingStatus = field(init = False, default = PublishingStatus.PUBLISHING)
    """The airing status of the manga."""
    published: DateRange = field(init = False)
    """To when and from this manga was aired."""
    score: float = field(init = False, default = 0.0)
    """The manga's score rating."""
    scored_by: int = field(init = False, default = 0)
    """Number of users that scored the manga."""

    def __post_init__(self):
        manga = self.data["data"]

        self.id = manga["mal_id"]
        self.url = manga["url"]
        self.image = Image(manga["images"])
        self.approved = manga["approved"]
        self.title = Title(manga["titles"])
        self.name = self.title

        self.chapters = manga.get("chapters")
        self.volumes = manga.get("volumes")
        
        status = manga.get("status")

        if status is not None:
            self.status = PublishingStatus(status)

        self.published = DateRange(manga["published"])
        self.score = manga["score"]
        self.scored_by = manga["scored_by"]


@dataclass
class FullManga(Manga):
    _get_endpoint = "/manga/{id}/full"

    data: JikanResponseData[FullMangaData] = field(repr=False)

    title_synonyms: List[str] = field(init = False)
    relations: RelationData = field(init = False)
    external: List[ExternalSourceData] = field(init = False)

    def __post_init__(self):
        super().__post_init__()
        manga = self.data["data"]

        self.title_synonyms = manga["title_synonyms"]
        self.relations = manga["relations"]
        self.external = manga["external"]