import datetime

import bson
from pymongo.collection import Collection

from domain.event import Event


class EventRepository:

    def __init__(self, db, collection_name):
        self._db = db
        self._collection_name = collection_name

    def insert(self, event: Event):
        event_collection = self._db[self._collection_name]  # type: Collection
        event_dict = event2dict(event)
        event_collection.insert_one(event_dict)

    def find(self, key):
        event_collection = self._db[self._collection_name]  # type: Collection
        res = event_collection.find(key)
        event_list = [dict2event(e) for e in res]
        return event_list

    def delete(self, key):
        event_collection = self._db[self._collection_name]  # type: Collection
        event_collection.delete_one(key)

    def update(self, key, event: Event):
        event_collection = self._db[self._collection_name]  # type: Collection
        event_collection.update_one(key, event2dict(event))


def event2dict(event: Event):
    if event.event_id:
        return {
            '_id': bson.ObjectId(event.event_id),
            'name': event.name,
            'date': event.date.isoformat(),
            'tags': event.tags
        }

    return {
            'name': event.name,
            'date': event.date.isoformat(),
            'tags': event.tags
        }


def dict2event(obj):
    return Event(str(obj['_id']), obj['name'], datetime.date.fromisoformat(obj['date']), obj['tags'])
