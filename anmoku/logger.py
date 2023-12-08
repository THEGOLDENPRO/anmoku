from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Literal, Optional

import logging
from devgoldyutils import add_custom_handler, Colours

__all__ = (
    "anmoku_logger", 
    "log_http_request"
)

anmoku_logger = add_custom_handler(
    logger = logging.getLogger(Colours.PURPLE.apply("anmoku")), 
    level = logging.WARNING
)

def log_http_request(method: Literal["GET"], url: str, logger: Optional[logging.Logger] = None) -> None:
    if logger is None:
        logger = anmoku_logger

    if method == "GET":
        logger.debug(f"{Colours.GREEN.apply('GET')} --> {url}")

    return None