from __future__ import annotations
from typing import TypedDict, final

__all__ = (
    "PartialPersonData",
)

class ImageData(TypedDict):
    image_url: str

@final
class ImagesData(TypedDict):
    jpg: ImageData


class PartialPersonData(TypedDict):
    mal_id: int
    url: str
    images: ImagesData
    name: str