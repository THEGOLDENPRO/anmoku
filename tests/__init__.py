import pytest
from anmoku.clients import AsyncAnmoku

__all__ = (
    "pytest",
    "client"
)

client = AsyncAnmoku(debug = True)