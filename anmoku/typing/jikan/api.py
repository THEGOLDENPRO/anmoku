from typing import TypedDict, TypeVar, Generic

__all__ = (
    "JikanResponseData",
    "JikanPageResponseData"
)

T = TypeVar("T")

class JikanResponseData(TypedDict, Generic[T]):
    """Typical Jikan response data."""
    data: T

class PaginationData(TypedDict):
    last_visible_page: int
    has_next_page: bool

class JikanPageResponseData(TypedDict, Generic[T]):
    """Jikan response data that contains pagination object."""
    data: T
    pagination: PaginationData