from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..typing.jikan import AnimeData, FullAnimeData, AnimeCharactersData, JikanResponseData

from dataclasses import dataclass

__all__ = (
    "Anime", 
    "FullAnime",
    "AnimeCharacters"
)

@dataclass
class Anime():
    _get_endpoint = "/anime/{id}"

    data: JikanResponseData[AnimeData]

@dataclass
class FullAnime(Anime):
    _get_endpoint = "/anime/{id}/full"

    data: JikanResponseData[FullAnimeData]


@dataclass
class AnimeCharacters():
    _get_endpoint = "/anime/{id}/characters"

    data: JikanResponseData[AnimeCharactersData]