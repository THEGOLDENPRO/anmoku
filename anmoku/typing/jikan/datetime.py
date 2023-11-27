from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict

if TYPE_CHECKING:
    from typing import Optional

__all__ = (
    "DateRangeData",
)

class DateData(TypedDict):
    day: int
    month: int
    year: int

DatePropData = TypedDict("DatePropData", {"from": DateData, "to": DateData})
DateRangeData = TypedDict("DateRange", {"from": Optional[str], "to": Optional[str], "prop": DatePropData})