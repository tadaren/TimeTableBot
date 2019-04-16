import datetime

from pymongo.collection import Collection

from domain.timetablechange import TimeTableChange


class TimeTableChangeRepository:
    def __init__(self, db, collection_name):
        self._db = db
        self._collection_name = collection_name

    def insert(self, change: TimeTableChange):
        change_collection = self._db[self._collection_name]  # type: Collection
        change_collection.insert_one(change2dict(change))

    def find(self, key):
        change_collection = self._db[self._collection_name]  # type: Collection
        res = change_collection.find(key)
        change_list = [dict2change(e) for e in res]
        return change_list

    def delete(self, key):
        change_collection = self._db[self._collection_name]  # type: Collection
        change_collection.delete_one(key)

    def update(self, key, change: TimeTableChange):
        change_collection = self._db[self._collection_name]  # type: Collection
        change_collection.update_one(key, change2dict(change))


def change2dict(time_table_change: TimeTableChange):
    if time_table_change.time_table_change_id:
        return {
            '_id': time_table_change.time_table_change_id,
            'date': time_table_change.date.isoformat(),
            'period': time_table_change.period,
            'subject': time_table_change.subject,
            'tags': time_table_change.tags
        }
    return {
        'date': time_table_change.date.isoformat(),
        'period': time_table_change.period,
        'subject': time_table_change.subject,
        'tags': time_table_change.tags
    }


def dict2change(obj):
    return TimeTableChange(obj['_id'], datetime.date.fromisoformat(obj['date']), obj['period'], obj['subject'], obj['tags'])
