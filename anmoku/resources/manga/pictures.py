from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Generator, Any

    from ...typing.jikan import (
        ImagesData, 
        JikanResponseData,
    )

from dataclasses import dataclass

from ..base import JikanIterableResource
from ..helpers import Image

__all__ = (
    "MangaPictures",
)

@dataclass
class MangaPictures(JikanIterableResource):
    _get_endpoint = "/manga/{id}/pictures"

    data: JikanResponseData[List[ImagesData]]
    
    def __post_init__(self):
        super().__post_init__(Image)

    def __next__(self) -> Image:
        return super().__next__()

    def __iter__(self) -> Generator[Image, Any, None]:
        return super().__iter__()