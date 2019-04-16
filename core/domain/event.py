from datetime import date
from dataclasses import dataclass


@dataclass
class Event:
    event_id: str
    name: str
    date: date
    tags: list
