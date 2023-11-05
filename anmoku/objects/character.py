from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..typing.jikan import JikanResponseData

from dataclasses import dataclass

__all__ = ("Character", "FullCharacter")

@dataclass
class Character():
    _endpoint = "/characters"

    data: JikanResponseData[dict]

@dataclass
class FullCharacter(Character):
    data: JikanResponseData[dict]