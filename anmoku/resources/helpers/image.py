from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from typing import Optional
    from typing_extensions import NotRequired

from dataclasses import dataclass, field

__all__ = ("Image",)

class ImageData(TypedDict):
    image_url: NotRequired[Optional[str]]
    small_image_url: NotRequired[Optional[str]]
    large_image_url: NotRequired[Optional[str]]

class ImagesData(TypedDict):
    jpg: ImageData
    webp: NotRequired[ImageData]

@dataclass
class Image():
    """A jikan image object."""
    data: ImagesData = field(repr = False)

    url: Optional[str] = field(init = False)
    """The url of this image."""

    def __post_init__(self):
        jpg_data = self.data.get("jpg")

        image_url = jpg_data.get("image_url")
        large_image_url = jpg_data.get("large_image_url")
        small_image_url = jpg_data.get("small_image_url")

        self.url = None

        if large_image_url is not None:
            self.url = large_image_url
        elif image_url is not None:
            self.url = image_url
        elif small_image_url is not None:
            self.url = small_image_url