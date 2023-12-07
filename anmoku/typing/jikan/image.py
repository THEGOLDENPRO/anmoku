from __future__ import annotations
from typing import TypedDict, final, Optional
from typing_extensions import NotRequired

__all__ = (
    "TrailerImagesData",
    "ImagesData"
)

class ImageData(TypedDict):
    image_url: NotRequired[Optional[str]]
    small_image_url: NotRequired[Optional[str]]
    large_image_url: NotRequired[Optional[str]]

@final
class TrailerImagesData(ImageData):
    medium_image_url: str
    maximum_image_url: str

@final
class ImagesData(TypedDict):
    jpg: ImageData
    webp: NotRequired[ImageData]