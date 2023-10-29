from __future__ import annotations

from .base_client import BaseClient, ConfigDict

class AsyncAnmoku(BaseClient):
    """Asynchronous anmoku client."""
    def __init__(self, config: ConfigDict = None) -> None:
        ...