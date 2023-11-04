from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..typing.jikan_api import JikanResponseData

from dataclasses import dataclass

__all__ = ("Character",)

@dataclass
class Character():
    _endpoint = "/characters"

    data: JikanResponseData[dict]