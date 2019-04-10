import datetime
from typing import List

import bson

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

    def get(self, first_day: datetime.date = None, last_day: datetime.date = None, tags: List[str] = []):
        query = {}
        date_query = build_date_query(first_day, last_day)
        if date_query:
            query['date'] = date_query
        if tags:
            query.update({'tag': {'$all': tags}})

        ret = self.repository.find(query)
        return ret

    def update(self, event_id, name, date, tag):
        self.repository.update({'_id': bson.ObjectId(event_id)}, Event(event_id, name, date, tag))

    def delete(self, event_id):
        self.repository.delete({'event_id': event_id})

    def add(self, name: str, date: datetime.date, tag: List[str]):
        self.repository.insert(Event('', name, date, tag))


def build_date_query(first_day: datetime.date = None, last_day: datetime.date = None):
    query = {}
    if first_day is not None:
        query.update({'$gte': first_day.isoformat()})
    if last_day is not None:
        query.update({'$lte': last_day.isoformat()})

    return query
