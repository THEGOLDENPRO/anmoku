from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..typing.jikan import JikanResponseData

from dataclasses import dataclass

from .base import JikanObject

__all__ = ("Character", "FullCharacter")

@dataclass
class Character(JikanObject):
    _get_endpoint = "/characters"

    data: JikanResponseData[dict]

@dataclass
class FullCharacter(Character):
    _get_endpoint = "/characters/{id}/full"

    data: JikanResponseData[dict]