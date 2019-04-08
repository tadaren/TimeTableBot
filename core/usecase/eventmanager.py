import datetime
from typing import List
from domain.event import Event


class EventManager:
    def __init__(self, repository):
        self.repository = repository

    def get_by_id(self, event_id):
        ret = self.repository.find({'event_id': event_id})
        return ret

    def get_by_day(self, first_day: datetime.date, last_day: datetime.date):
        ret = self.repository.find(
            {
                'date':
                {
                    '$gte': first_day.isoformat(),
                    '$lte': last_day.isoformat()
                }
            }
        )
        return ret

    def get_by_tags(self, tag: List[str]):
        ret = self.repository.find(
            {
                'tag': {
                    '$all': tag
                }
            }
        )
        return ret

    def update(self, event_id, name, date, tag):
        pass

    def delete(self, event_id):
        pass

    def add(self, name: str, date: datetime.date, tag: List[str]):
        self.repository.insert(Event(0, name, date, tag))
