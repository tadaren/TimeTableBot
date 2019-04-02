from datetime import date
from dataclasses import dataclass


@dataclass
class Event:
    event_id: int
    name: str
    date: date
    tag: list
