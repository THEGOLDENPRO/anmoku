from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from .image import ImageData

__all__ = (
    "PartialUserData",
)

class PartialUserData(TypedDict):
    username: str
    url: str
    images: ImageData