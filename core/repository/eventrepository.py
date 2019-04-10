import bson
from pymongo.collection import Collection

from domain.event import Event


class EventRepository:

    def __init__(self, db, collection_name):
        self._db = db
        self._collection_name = collection_name

    def insert(self, event: Event):
        event_collection = self._db[self._collection_name]
        event_dict = event_to_dict(event)
        event_collection.insert_one(event_dict)

    def find(self, key):
        event_collection = self._db[self._collection_name]
        res = event_collection.find(key)
        event_list = [dict_to_event(e) for e in res]
        return event_list

    def delete(self, key):
        event_collection = self._db[self._collection_name]
        event_collection.delete_one(key)

    def update(self, key, event: Event):
        event_collection = self._db[self._collection_name]
        event_collection.update_one(key, event_to_dict(event))


def event_to_dict(event: Event):
    if event.event_id:
        return {
            '_id': bson.ObjectId(event.event_id),
            'name': event.name,
            'date': event.date.isoformat(),
            'tag': event.tag
        }

    return {
            'name': event.name,
            'date': event.date.isoformat(),
            'tag': event.tag
        }


def dict_to_event(obj):
    return Event(str(obj['_id']), obj['name'], obj['date'], obj['tag'])
