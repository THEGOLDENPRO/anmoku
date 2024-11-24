from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

    from ...typing.jikan import (
        ImagesData, 
        JikanResponseData,
    )

from dataclasses import dataclass, field

from ..base import JikanResource
from ..helpers import Image

__all__ = (
    "MangaPictures",
)

@dataclass
class MangaPictures(JikanResource):
    _get_endpoint = "/manga/{id}/pictures"

    data: JikanResponseData[List[ImagesData]] = field(repr = False)
    
    def __iter__(self):
        for picture in self.data["data"]:
            yield Image(picture)