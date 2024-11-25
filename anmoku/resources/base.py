from __future__ import annotations
from typing import TYPE_CHECKING, Any, Optional, TypeVar, List, Type

if TYPE_CHECKING:
    from typing import Generator

    from ..typing.jikan import JikanResponseData

from dataclasses import dataclass, field

__all__ = (
    "JikanResource",
    "JikanIterableResource"
)

T = TypeVar("T")

@dataclass
class JikanResource():
    _get_endpoint: Optional[str] = field(init = False, repr = False, default = None)
    """The jikan api endpoint where you can get this object."""
    _search_endpoint: Optional[str] = field(init = False, repr = False, default = None)
    """The jikan api endpoint to search with this resource."""
    _random_endpoint: Optional[str] = field(init = False, repr = False, default = None)
    """The jikan api endpoint to get a random object with this resource."""

    data: JikanResponseData[Any]

@dataclass
class JikanIterableResource(JikanResource):
    __object: Type[T] = field(repr = False, init = False)
    __object_iter: List[Any] = field(repr = False, init = False)

    def __post_init__(self, object: object):
        self.__object = object
        self.__object_iter = iter(self.data["data"])

    def __next__(self) -> T:
        return self.__object(
            next(self.__object_iter)
        )

    def __iter__(self) -> Generator[T, Any, None]:

        for data in self.__object_iter:
            yield self.__object(data)