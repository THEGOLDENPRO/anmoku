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

    from_: Optional[datetime] = field(init = False, default = None)
    """The date and time the range starts from."""
    to: Optional[datetime] = field(init = False, default = None)
    """The date and time the range ends at."""

    def __post_init__(self):
        from_iso_string = self.data["from"]
        to_iso_string = self.data["to"]

        if from_iso_string is not None:
            self.from_ = datetime.fromisoformat(from_iso_string)

            if to_iso_string is None:
                self.to = self.from_

        if to_iso_string is not None:
            self.to = datetime.fromisoformat(to_iso_string)