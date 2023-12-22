from __future__ import annotations
from typing import TypedDict, final, List

from ..person import PartialPersonData

__all__ = (
    "AnimeStaffData",
)

@final
class AnimeStaffData(TypedDict):
    person: PartialPersonData
    positions: List[str]