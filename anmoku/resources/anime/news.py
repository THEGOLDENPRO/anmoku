from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

    from ...typing.jikan import (
        NewsData, 
        JikanResponseData,
    )

from dataclasses import dataclass, field

from ..base import JikanResource
from ..helpers import News

__all__ = (
    "AnimeNews",
)

@dataclass
class AnimeNews(JikanResource):
    _get_endpoint = "/anime/{id}/news"

    data: JikanResponseData[List[NewsData]] = field(repr = False)
    
    def __iter__(self):
        for news in self.data["data"]:
            yield News(news)