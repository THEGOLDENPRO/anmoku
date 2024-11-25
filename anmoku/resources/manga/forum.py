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
    "MangaTopics",
    "MangaForum"
)


@dataclass
class MangaTopics(JikanResource):
    _get_endpoint = "/manga/{id}/forum"

    data: JikanResponseData[List[ForumData]] = field(repr = False)

    def __iter__(self):
        for forum in self.data["data"]:
            yield Forum(forum)

MangaForum = MangaTopics