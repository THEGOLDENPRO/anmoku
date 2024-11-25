from dataclasses import dataclass

__all__ = (
    "Author",
)

@dataclass
class Author():
    url: str
    """The profile URL of the author"""
    username: str
    """The username of the author."""