from __future__ import annotations
from typing import TYPE_CHECKING, List

if TYPE_CHECKING:
    from ...typing.jikan.manga.statistics import ScoresData
    from ...typing.jikan import (
        MangaStatisticsData, 
        JikanResponseData,
    )

from dataclasses import dataclass, field

from ..base import JikanResource

__all__ = (
    "MangaStatistics",
)

@dataclass
class Scores:
    data: ScoresData = field(repr=False)

    score: int = field(init = False)
    votes: int = field(init = False)
    percentage: int = field(init = False)

    def __post_init__(self):
        self.score = self.data["score"]
        self.votes = self.data["votes"]
        self.percentage = self.data["percentage"]

@dataclass
class MangaStatistics(JikanResource):
    _get_endpoint = "/manga/{id}/statistics"

    data: JikanResponseData[MangaStatisticsData] = field(repr=False)

    reading: int = field(init = False)
    completed: int = field(init = False)
    on_hold: int = field(init = False)
    dropped: int = field(init = False)
    plan_to_read: int = field(init = False)
    total: int = field(init = False)
    scores: List[Scores] = field(init = False)

    def __post_init__(self):
        stats = self.data["data"]

        self.reading = stats["reading"]
        self.completed = stats["completed"]
        self.on_hold = stats["on_hold"]
        self.dropped = stats["dropped"]
        self.plan_to_read = stats["plan_to_read"]
        self.total = stats["total"]
        self.scores = []

        for scores in stats["scores"]:
            self.scores.append(
                Scores(scores)
            )