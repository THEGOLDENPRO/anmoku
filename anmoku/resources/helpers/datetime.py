from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional

    from ...typing.jikan.datetime import DateRangeData

from datetime import datetime
from dataclasses import dataclass, field

__all__ = ("DateRange",)

@dataclass()
class DateRange():
    """A jikan date range helper."""
    data: DateRangeData = field(repr = False)

    from_: Optional[datetime] = field(init = False)
    """The date and time the range starts from."""
    to: Optional[datetime] = field(init = False)
    """The date and time the range ends at."""

    def __post_init__(self):
        self.from_ = None
        self.to = None
        ... # TODO: Finish this.