from datetime import date
from dataclasses import dataclass


@dataclass
class Event:
    event_id: str
    name: str
    date: date
    tags: list


def event2dict(event: Event):
    return {
        'id': str(event.event_id),
        'name': event.name,
        'date': event.date.isoformat(),
        'tags': event.tags
    }
