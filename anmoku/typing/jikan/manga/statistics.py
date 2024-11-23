from __future__ import annotations
from typing import List, TypedDict

__all__ = (
    "MangaStatisticsData",
)

class ScoresData(TypedDict):
    score: int
    votes: int
    percentage: int

class MangaStatisticsData(TypedDict):
    reading: int
    completed: int
    on_hold: int
    dropped: int
    plan_to_read: int
    total: int
    scores: List[ScoresData]
