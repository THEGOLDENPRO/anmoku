from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...typing.jikan import (
        AnimeData, 
        FullAnimeData, 
        JikanResponseData
    )

from dataclasses import dataclass

from ..base import JikanObject

__all__ = (
    "Anime", 
    "FullAnime"
)

@dataclass
class Anime(JikanObject):
    _get_endpoint = "/anime/{id}"

    data: JikanResponseData[AnimeData]

@dataclass
class FullAnime(Anime):
    _get_endpoint = "/anime/{id}/full"

    data: JikanResponseData[FullAnimeData]