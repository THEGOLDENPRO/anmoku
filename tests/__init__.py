from __future__ import annotations
from typing import TYPE_CHECKING

if TYPE_CHECKING:
    from typing import Type, List
    from anmoku.clients.base import ResourceGenericT

import time
import pytest
import inspect
import asyncio
from anmoku.clients import AsyncAnmoku, Anmoku
from anmoku.resources import * # this MUST be a star import

from slowstack.asynchronous.all import AllRateLimiter
from slowstack.asynchronous.times_per import TimesPerRateLimiter

__all__ = (
    "pytest",
    "client",
    "async_client",
    "wait_after",
    "get_all_resource_classes"
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

def get_all_resource_classes() -> List[Type[ResourceGenericT]]:
    resources = []

    for _, _object in globals().items():

        if not inspect.isclass(_object):
            continue

        if issubclass(_object, JikanResource):
            resource = _object

            if resource._get_endpoint is None:
                continue

            resources.append(resource)

    return resources