from typing import TYPE_CHECKING

if TYPE_CHECKING:
    ...

from dataclasses import dataclass

__all__ = ("Character",)

@dataclass
class Character():
    _endpoint = "/characters"

    data: dict