from typing import TypedDict, TypeVar, Generic

__all__ = ("JikanResponseData",)

T = TypeVar("T")

class JikanResponseData(TypedDict, Generic[T]):
    data: T