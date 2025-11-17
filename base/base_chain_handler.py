from __future__ import annotations
from abc import ABC, abstractmethod


class BaseHandler(ABC):
    def __init__(self):
        self._next: BaseHandler | None = None

    def set_next(self, handler: BaseHandler) -> BaseHandler:
        self._next = handler
        return handler

    def run_next(self, data):
        if self._next:
            return self._next.handle(data)
        return data

    @abstractmethod
    def handle(self, data):
        pass
