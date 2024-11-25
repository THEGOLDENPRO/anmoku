from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Generator, Any, Optional

    from ...typing.jikan.manga import MangaUserUpdatesData
    from ...typing.jikan.api import JikanResponseData

from dataclasses import dataclass, field
from datetime import datetime

from ..base import JikanIterableResource
from ..helpers import User

__all__ = (
    "MangaUserUpdates",
)

@dataclass
class UserUpdate():
    data: MangaUserUpdatesData

    user: User = field(init = False)
    """The user in this update."""
    score: Optional[int] = field(init = False)
    """The score the user gave the manga."""
    status: str = field(init = False)
    """The status, e.g. `Completed`."""
    volumes_read: int = field(init = False)
    """The amount of volumes read."""
    total_volumes: int = field(init = False)
    """The amount of total volumes."""
    chapters_read: int = field(init = False)
    """The amount of chapters read."""
    total_chapters: int = field(init = False)
    """The amount of total chapters."""
    date: datetime = field(init = False)
    """When the update was made."""

    def __post_init__(self):
        update = self.data

        self.user = User(update["user"])
        self.score = update["score"]
        self.status = update["status"]
        self.volumes_read = update["volumes_read"]
        self.total_volumes = update["volumes_total"]
        self.chapters_read = update["chapters_read"]
        self.total_chapters = update["chapters_total"]
        self.date = datetime.fromisoformat(update["date"])

@dataclass
class MangaUserUpdates(JikanIterableResource):
    _get_endpoint = "/manga/{id}/userupdates"

    data: JikanResponseData[List[MangaUserUpdatesData]]

    def __post_init__(self):
        super().__post_init__(UserUpdate)

    def __next__(self) -> UserUpdate:
        return super().__next__()

    def __iter__(self) -> Generator[UserUpdate, Any, None]:
        return super().__iter__()