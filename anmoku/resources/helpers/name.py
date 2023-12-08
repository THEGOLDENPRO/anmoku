from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Optional

    from ...typing.jikan import NameData

from dataclasses import dataclass, field

__all__ = ("Name",)

@dataclass
class Name():
    """A jikan name object."""
    data: NameData = field(repr = False)

    default: str = field(init = False)
    """The default name."""
    kanji: Optional[str] = field(init = False, default = None)
    """The name in japanese kanji."""

    def __post_init__(self):
        self.default = self.data["name"]

        kanji_name = self.data.get("name_kanji")

        if kanji_name is not None:
            self.kanji = kanji_name

    def __str__(self) -> str:
        return self.default