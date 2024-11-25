from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Generator, Any

    from ...typing.jikan import (
        NewsData, 
        JikanResponseData,
    )

from dataclasses import dataclass

from ..base import JikanIterableResource
from ..helpers import News

__all__ = (
    "AnimeNews",
)

@dataclass
class AnimeNews(JikanIterableResource):
    _get_endpoint = "/anime/{id}/news"

    data: JikanResponseData[List[NewsData]]

    def __post_init__(self):
        super().__post_init__(News)

    def __next__(self) -> News:
        return super().__next__()

    def __iter__(self) -> Generator[News, Any, None]:
        return super().__iter__()