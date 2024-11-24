from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import List, Optional

    from ...typing.jikan import TitleData

from dataclasses import dataclass, field

__all__ = ("Title",)

@dataclass
class Title():
    """A jikan title object."""
    data: List[TitleData] = field(repr = False)

    default: str = field(init = False)
    """The default title."""
    english: Optional[str] = field(init = False, default = None)
    """The english title."""
    japanese: Optional[str] = field(init = False, default = None)
    """The japanese title."""
    synonyms: List[str] = field(init = False)
    """A list of synonym titles."""

    def __post_init__(self):
        self.synonyms = []

        for title in self.data:

            if title["type"] == "Default":
                self.default = title["title"]
            elif title["type"] == "English":
                self.english = title["title"]
            elif title["type"] == "Japanese":
                self.japanese = title["title"]
            elif title["type"] == "Synonym":
                self.synonyms.append(title["title"])

    def __str__(self) -> str:
        return self.default

    @classmethod
    def _from_old_title_data(
        cls,
        default_title: str,
        japanese_title: Optional[str],
        romanji_title: Optional[str]
    ):
        titles: List[TitleData] = []

        if japanese_title is not None:
            titles.append(
                {"type": "Japanese", "title": japanese_title}
            )

        if romanji_title is not None:
            titles.append(
                {"type": "Japanese", "title": romanji_title}
            )

        titles.append(
            {"type": "Default", "title": default_title}
        )

        return cls(titles)