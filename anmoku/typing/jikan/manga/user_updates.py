from __future__ import annotations
from typing import TypedDict, TYPE_CHECKING, Optional

if TYPE_CHECKING:
    from .. import PartialUserData

__all__ = (
    "MangaUserUpdatesData",
)

class MangaUserUpdatesData(TypedDict):
    user: PartialUserData
    score: Optional[int]
    status: str
    volumes_read: int
    volumes_total: int
    chapters_read: int
    chapters_total: int
    date: str
