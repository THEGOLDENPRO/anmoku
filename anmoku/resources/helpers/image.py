from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional
    from ...typing.jikan import ImagesData, TrailerImagesData

import io
import requests
from PIL import Image as PillowImage
from dataclasses import dataclass, field
from devgoldyutils import LoggerAdapter, Colours

from ...logger import anmoku_logger

__all__ = ("Image",)

logger = LoggerAdapter(anmoku_logger, prefix = "Image")

@dataclass
class Image():
    """A jikan image object."""
    data: ImagesData | TrailerImagesData = field(repr = False)

    url: Optional[str] = field(init = False, default = None)
    """The url of this image."""

    def __post_init__(self):
        jpg_data = self.data.get("jpg", {})

        image_url = jpg_data.get("image_url")
        large_image_url = jpg_data.get("large_image_url")
        small_image_url = jpg_data.get("small_image_url")

        medium_image_url = self.data.get("medium_image_url")
        maximum_image_url = self.data.get("maximum_image_url")

        if maximum_image_url is not None:
            self.url = maximum_image_url
        elif large_image_url is not None:
            self.url = large_image_url
        elif medium_image_url is not None:
            self.url = medium_image_url
        elif image_url is not None:
            self.url = image_url
        elif small_image_url is not None:
            self.url = small_image_url

    def get_image(self) -> Optional[PillowImage.Image]:
        """Makes request to the url and returns the image as a Pillow Image object. Returns None if the url request made wasn't okay."""
        if self.url is None:
            return None

        logger.debug(f"{Colours.GREEN.apply('GET')} --> {self.url}")

        r = requests.get(self.url)

        if r.ok is False:
            return None

        return PillowImage.open(io.BytesIO(r.content))