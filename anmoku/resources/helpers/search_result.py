from __future__ import annotations
from typing import TYPE_CHECKING, Generic, TypeVar

if TYPE_CHECKING:
    from typing import Any, Type, Generator
    from ...typing.jikan import SearchResultData

from dataclasses import dataclass, field

from ..base import JikanResource

A = TypeVar(
    "A", 
    bound = JikanResource
)

__all__ = ("SearchResult",)

@dataclass
class SearchResult(Generic[A]):
    data: SearchResultData[Any] = field(repr = False)
    resource: Type[A] = field(repr = False)

    def __post_init__(self):
        # TODO: Add pagination attribute.
        ...

    def __iter__(self) -> Generator[A, Any, None]:

        for result in self.data["data"]:
            yield self.resource({"data": result})