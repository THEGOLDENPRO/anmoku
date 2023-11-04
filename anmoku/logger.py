import logging
from devgoldyutils import add_custom_handler, Colours

__all__ = ("anmoku_logger",)

anmoku_logger = add_custom_handler(
    logger = logging.getLogger(Colours.PURPLE.apply("anmoku")), 
    level = logging.WARNING
)