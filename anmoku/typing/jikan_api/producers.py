from __future__ import annotations
from typing import TYPE_CHECKING, TypedDict, final

if TYPE_CHECKING:
    ...

__all__ = ("Producer",)

class Producer(TypedDict):
    mal_id: int
    type: str
    name: str
    url: str