from __future__ import annotations
from typing import TypedDict, TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List

    from .user import PartialUserData

__all__ = (
    "ReviewData",
)

class ReactionsData(TypedDict):
    overall: int
    nice: int
    love_it: int
    funny: int
    confusing: int
    informative: int
    well_written: int
    creative: int

class ReviewData(TypedDict):
    user: PartialUserData
    mal_id: int
    url: str
    type: str
    reactions: ReactionsData
    date: str
    review: str
    score: int
    tags: List[str]
    is_spoiler: bool
    is_preliminary: bool