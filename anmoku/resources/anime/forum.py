from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Generator, Any

    from ...typing.jikan import (
        ForumData, 
        JikanResponseData,
    )

from dataclasses import dataclass

from ..base import JikanIterableResource
from ..helpers import Forum

__all__ = (
    "AnimeTopics",
    "AnimeForum"
)

@dataclass
class AnimeForum(JikanIterableResource):
    _get_endpoint = "/anime/{id}/forum"

    data: JikanResponseData[List[ForumData]]
    
    def __post_init__(self):
        super().__post_init__(Forum)

    def __next__(self) -> Forum:
        return super().__next__()

    def __iter__(self) -> Generator[Forum, Any, None]:
        return super().__iter__()

AnimeTopics = AnimeForum