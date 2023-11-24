from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ..typing.jikan import JikanResponseData

from dataclasses import dataclass, field

__all__ = ("JikanResource",)

@dataclass
class JikanResource():
    _get_endpoint: Optional[str] = field(init = False, default = None)
    """The jikan api endpoint where you can get this object."""

    data: JikanResponseData[Any]