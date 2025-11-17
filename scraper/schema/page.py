from dataclasses import dataclass


@dataclass
class PageContext:
    url: str
    number: int
