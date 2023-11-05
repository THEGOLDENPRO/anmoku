from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from ..typing.jikan import JikanResponseData

from dataclasses import dataclass, field

__all__ = ("JikanObject",)

@dataclass
class JikanObject():
    _get_endpoint: str = field(init = False, default = None)
    """The jikan api endpoint where you can get this object."""

    data: JikanResponseData[dict]