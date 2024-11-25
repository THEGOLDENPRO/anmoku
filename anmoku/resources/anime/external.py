from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

    from ...typing.jikan import (
        ExternalSourceData,
        JikanResponseData,
    )

from dataclasses import dataclass, field

from ..base import JikanResource
from ..helpers import ExternalSource

__all__ = (
    "AnimeExternal",
)

@dataclass
class AnimeExternal(JikanResource):
    _get_endpoint = "/anime/{id}/external"

    data: JikanResponseData[List[ExternalSourceData]] = field(repr = False)
    
    def __iter__(self):
        for relation in self.data["data"]:
            yield ExternalSource(relation)