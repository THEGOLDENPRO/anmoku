from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

    from ...typing.jikan import (
        ForumData, 
        JikanResponseData,
    )

from dataclasses import dataclass, field

from ..base import JikanResource
from ..helpers import Forum

__all__ = (
    "AnimeTopics",
    "AnimeForum"
)


@dataclass
class AnimeForum(JikanResource):
    _get_endpoint = "/anime/{id}/forum"

    data: JikanResponseData[List[ForumData]] = field(repr = False)
    
    def __iter__(self):
        for forum in self.data["data"]:
            yield Forum(forum)

AnimeTopics = AnimeForum