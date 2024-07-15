from __future__ import annotations

import time
import pytest
import asyncio
from anmoku.clients import AsyncAnmoku, Anmoku

from slowstack.asynchronous.all import AllRateLimiter
from slowstack.asynchronous.times_per import TimesPerRateLimiter

__all__ = (
    "pytest",
    "client",
    "async_client",
    "wait_after"
)

client = Anmoku(debug = True)
client._minute_rate_limiter.limit = 30

async_client = AsyncAnmoku(debug = True)
async_client._rate_limiter = AllRateLimiter(
    {
        TimesPerRateLimiter(3, 3), 
        TimesPerRateLimiter(30, 60) # half the 
    }
)

def wait_after(seconds: int, is_async: bool = False):

    def outer(func):

        if is_async:

            async def inner(*args, **kwargs) -> None:
                await func(*args, **kwargs)

                await asyncio.sleep(seconds)

            return inner

        def inner(*args, **kwargs) -> None:
            func(*args, **kwargs)

            time.sleep(seconds)

        return inner

    return outer