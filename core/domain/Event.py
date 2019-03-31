import datetime
from dataclasses import dataclass


@dataclass
class Event:
    event_id: int
    name: str
    date: datetime
    tag: list
