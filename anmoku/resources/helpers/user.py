from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...typing.jikan import PartialUserData

from dataclasses import dataclass, field

from .image import Image

__all__ = (
    "User",
)

@dataclass
class User():
    data: PartialUserData = field(repr = False)

    username: str = field(init = False)
    """The MyAnimeList Username of the reviewer."""
    url: str = field(init = False)
    """The MyAnimeList Profile URL of the reviewer."""
    image: Image = field(init = False)
    """The Profile Picture of the reviewer."""

    def __post_init__(self):
        user = self.data

        self.username = user["username"]
        self.url = user["url"]
        self.image = Image(user["images"])