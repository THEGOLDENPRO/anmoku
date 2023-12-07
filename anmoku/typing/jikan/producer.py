from __future__ import annotations
from typing import TypedDict

__all__ = ("Producer",)

class Producer(TypedDict):
    mal_id: int
    type: str
    name: str
    url: str