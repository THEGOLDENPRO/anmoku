from __future__ import annotations
from typing import TypedDict, Optional

__all__ = (
    "DateRangeData",
)

class DateData(TypedDict):
    day: int
    month: int
    year: int

DatePropData = TypedDict("DatePropData", {"from": DateData, "to": DateData})
DateRangeData = TypedDict("DateRange", {"from": Optional[str], "to": Optional[str], "prop": DatePropData})