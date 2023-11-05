from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, final

if TYPE_CHECKING:
    ...

__all__ = (
    "PartialCharacter",
)

class ImageData(TypedDict):
    image_url: str
    small_image_url: str

@final
class ImagesData(TypedDict):
    jpg: ImageData
    webp: ImageData


class PartialCharacter(TypedDict):
    mal_id: int
    url: str
    images: ImagesData
    name: str