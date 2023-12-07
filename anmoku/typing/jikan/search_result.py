from __future__ import annotations
from typing import TypedDict, Generic, TypeVar, List

__all__ = (
    "SearchResultData",
)

T = TypeVar("T")

class SearchResultData(TypedDict, Generic[T]):
    data: List[T]
    pagination: PaginationData


PaginationItem = TypedDict("PaginationItems", {"count": int, "total": int, "per_page": int})

class PaginationData(TypedDict):
    last_visible_page: int
    has_next_page: bool
    items: List[PaginationItem]