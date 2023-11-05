from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, final

if TYPE_CHECKING:
    ...

__all__ = (
    "PartialPerson",
)

class ImageData(TypedDict):
    image_url: str

@final
class ImagesData(TypedDict):
    jpg: ImageData


class PartialPerson(TypedDict):
    mal_id: int
    url: str
    images: ImagesData
    name: str