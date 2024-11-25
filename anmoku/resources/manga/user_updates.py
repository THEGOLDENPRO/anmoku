from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from ...typing.jikan.manga import MangaUserUpdatesData
    from ...typing.jikan.api import JikanResponseData

from dataclasses import dataclass, field
from datetime import datetime

from ..base import JikanResource
from ..helpers import User

__all__ = (
    "MangaUserUpdates",
)

@dataclass
class UserUpdate():
    data: MangaUserUpdatesData

    user: User = field(init = False)
    """The user in this update."""
    score: int = field(init = False)
    """The score the user gave the manga."""
    status: str = field(init = False)
    """The status, e.g. `Completed`."""
    volumes_read: int = field(init = False)
    """The amount of volumes read."""
    volumes_total: int = field(init = False)
    """The amount of total volumes."""
    chapters_read: int = field(init = False)
    """The amount of chapters read."""
    chapters_total: int = field(init = False)
    """The amount of total chapters."""
    date: datetime = field(init = False)
    """When the update was made."""

    def __post_init__(self):
        update = self.data

        self.user = User(update["user"])
        self.score = update["score"]
        self.status = update["status"]
        self.volumes_read = update["volumes_read"]
        self.volumes_total = update["volumes_total"]
        self.chapters_read = update["chapters_read"]
        self.chapters_total = update["chapters_total"]
        self.date = datetime.fromisoformat(update["date"])

@dataclass
class MangaUserUpdates(JikanResource):
    _get_endpoint = "/manga/{id}/userupdates"

    data: JikanResponseData[List[MangaUserUpdatesData]] = field(repr = False)

    def __iter__(self):

        for update in self.data["data"]:
            yield UserUpdate(update)