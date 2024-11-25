from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ...typing.jikan import (
        ExternalSourceData,
    )

from dataclasses import dataclass, field

__all__ = (
    "ExternalSource",
)

@dataclass
class ExternalSource():
    data: ExternalSourceData = field(repr = False)

    name: str = field(init = False)
    url: str = field(init = False)

    def __post_init__(self):
        external = self.data

        self.name = external["name"]
        self.url = external["url"]