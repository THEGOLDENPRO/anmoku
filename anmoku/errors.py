from __future__ import annotations
from typing import TYPE_CHECKING, Optional, TypedDict

if TYPE_CHECKING:
    from typing import Type
    from logging import Logger
    from typing_extensions import NotRequired

    from .resources import JikanResource

from .logger import anmoku_logger
from devgoldyutils import Colours

__all__ = (
    "HTTPError",
    "NotFoundError",
    "RatelimitError",
    "ServerError",
    "ResourceNotSupportedError"
)

class ErrorResponseDict(TypedDict):
    status: int
    type: str
    message: str
    error: str
    report_url: NotRequired[str]

class AnmokuException(Exception):
    def __init__(self, message: str, logger: Logger = None):
        message = Colours.RED.apply_to_string(message)

        if logger is None:
            logger = anmoku_logger

        logger.critical(message)
        super().__init__(message)


class HTTPError(AnmokuException):
    __slots__ = (
        "status",
        "type",
        "message",
        "report_url",
    )

    def __init__(self, resp: ErrorResponseDict):
        self.status: int = resp["status"]
        self.type: str = resp["type"]
        self.message: str = resp["message"]
        self.report_url: Optional[str] = resp.get("report_url")
        # TODO: error trace?

        msg = f"{self.type} (status code {self.status}): {self.message}"

        if self.report_url is not None:
            msg += f"\nYou can report this issue to the Jikan GitHub via this link: {self.report_url}"

        super().__init__(msg)


class NotFoundError(HTTPError):
    __slots__ = ()


class RatelimitError(HTTPError):
    __slots__ = ()


class ServerError(HTTPError):
    __slots__ = ()


class ResourceNotSupportedError(AnmokuException):
    def __init__(self, resource: Type[JikanResource], not_supported: str, logger: Logger = None):
        super().__init__(
            f"The '{resource.__name__}' resource does not support {not_supported}!", 
            logger
        )