from __future__ import annotations
from typing import TYPE_CHECKING, TypeVar

if TYPE_CHECKING:
    from typing import Optional, Callable, Any

import time
import asyncio
from devgoldyutils import LoggerAdapter

from ..logger import anmoku_logger

__all__ = (
    "RateLimitHandler",
)

T = TypeVar("T")

logger = LoggerAdapter(anmoku_logger, prefix = "RateLimitHandler")

class RateLimitHandler():
    def __init__(
        self, 
        requests_per_second_limit: Optional[int] = None,
        requests_per_minute_limit: Optional[int] = None
    ):
        self.requests_per_second_limit = requests_per_second_limit or 3
        self.requests_per_minute_limit = requests_per_minute_limit or 60

        self._second_requests_count = 0
        self._minute_requests_count = 0

        self._last_request_time = 0

    def wait_for_rate_limit(self):
        current_time = time.time_ns()
        self._update_time(current_time)

        # Check if the requests per minute limit is reached.
        if self._minute_requests_count >= self.requests_per_minute_limit:
            logger.debug("Exceeded rate limit, waiting for 60 seconds...")
            time.sleep(60)
            self._minute_requests_count = 0
            self._last_request_time = time.time_ns()

        # Check if the requests per second limit is reached.
        if self._second_requests_count >= self.requests_per_second_limit:
            logger.debug("Exceeded 3 requests per second rate limit, waiting for 1 second...")
            time.sleep(1)
            self._second_requests_count = 0
            self._last_request_time = time.time_ns()

        self._second_requests_count += 1
        self._minute_requests_count += 1

    async def async_wait_for_rate_limit(self):
        current_time = time.time_ns()
        self._update_time(current_time)

        # Check if the requests per minute limit is reached.
        if self._minute_requests_count >= self.requests_per_minute_limit:
            logger.debug("Exceeded rate limit, waiting for 60 seconds...")
            await asyncio.sleep(60)
            self._minute_requests_count = 0
            self._last_request_time = time.time_ns()

        # Check if the requests per second limit is reached.
        if self._second_requests_count >= self.requests_per_second_limit:
            logger.debug("Exceeded 3 requests per second rate limit, waiting for 1 second...")
            await asyncio.sleep(1)
            self._second_requests_count = 0
            self._last_request_time = time.time_ns()

        self._second_requests_count += 1
        self._minute_requests_count += 1

    def _update_time(self, current_time: float):
        elapsed_time = (current_time - self._last_request_time) / (10 ** 9)

        if elapsed_time >= 60:
            self._minute_requests_count = 0
            self._last_request_time = current_time

        if elapsed_time >= 2:
            self._second_requests_count = 0
            self._last_request_time = current_time