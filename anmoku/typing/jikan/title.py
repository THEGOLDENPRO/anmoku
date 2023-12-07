from __future__ import annotations
from typing import TypedDict, Literal

__all__ = (
    "TitleData",
)

class TitleData(TypedDict):
    type: Literal["Default", "Synonym", "Japanese", "English", "German", "Spanish", "French"]
    title: str