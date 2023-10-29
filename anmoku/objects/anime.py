from typing import TYPE_CHECKING

if TYPE_CHECKING:
    ...

from dataclasses import dataclass

__all__ = ("Anime",)

@dataclass
class Anime():
    data: dict