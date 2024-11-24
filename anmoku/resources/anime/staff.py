from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List
    from ...typing.jikan import (
        AnimeStaffData, 
        JikanResponseData
    )

from dataclasses import dataclass, field

from ..helpers import Image
from ..base import JikanResource

__all__ = (
    "AnimeStaff",
)

@dataclass
class AnimeStaff(JikanResource):
    """Get data of the staff from a particular anime."""
    _get_endpoint = "/anime/{id}/staff"

    data: JikanResponseData[List[AnimeStaffData]]

    def __iter__(self):

        for staff in self.data["data"]:
            yield AnimeIndividualStaff(staff)

@dataclass
class AnimeIndividualStaff():
    data: AnimeStaffData

    id: int = field(init = False)
    """The MyAnimeList ID of this staff."""
    name: str = field(init = False)
    """The name of this staff."""
    url: str = field(init = False)
    """The MyAnimeList URL to this staff."""
    image: Image = field(init = False)
    """The image of this staff."""

    positions: List[str] = field(init = False)
    """The list of positions this staff possess."""

    def __post_init__(self):
        person = self.data["person"]

        self.id = person["mal_id"]
        self.name = person["name"]
        self.url = person["url"]
        self.image = Image(person["images"])

        self.positions = self.data["positions"]