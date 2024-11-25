from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Generator, Any

    from ...typing.jikan import (
        ExternalSourceData,
        JikanResponseData,
    )

from dataclasses import dataclass

from ..base import JikanIterableResource
from ..helpers import ExternalSource

__all__ = (
    "AnimeExternal",
)

@dataclass
class AnimeExternal(JikanIterableResource):
    _get_endpoint = "/anime/{id}/external"

    data: JikanResponseData[List[ExternalSourceData]]
    
    def __post_init__(self):
        super().__post_init__(ExternalSource)

    def __next__(self) -> ExternalSource:
        return super().__next__()

    def __iter__(self) -> Generator[ExternalSource, Any, None]:
        return super().__iter__()