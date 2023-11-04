from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..typing.jikan_api import AnimeData, FullAnimeData, JikanResponseData

from dataclasses import dataclass

__all__ = ("Anime", "FullAnime")

@dataclass
class Anime():
    _endpoint = "/anime"

    data: JikanResponseData[AnimeData]

@dataclass
class FullAnime(Anime):
    data: JikanResponseData[FullAnimeData]