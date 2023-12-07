from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional

if TYPE_CHECKING:
    from ..typing.jikan import JikanResponseData

from dataclasses import dataclass, field

__all__ = ("JikanResource",)

@dataclass
class JikanResource():
    _get_endpoint: Optional[str] = field(init = False, default = None) # TODO: Check if this has to be optional.
    """The jikan api endpoint where you can get this object."""
    _search_endpoint: Optional[str] = field(init = False, default = None)
    """The jikan api endpoint to search with this resource."""

    data: JikanResponseData[Any]