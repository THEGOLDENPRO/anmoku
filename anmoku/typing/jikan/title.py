from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from typing import Literal

__all__ = (
    "TitleData",
)

class TitleData(TypedDict):
    type: Literal["Default", "Synonym", "Japanese", "English", "German", "Spanish", "French"]
    title: str