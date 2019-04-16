import datetime

from pymongo.collection import Collection

from domain.timetable import TimeTable


class TimeTableRepository:
    def __init__(self, db, collection_name):
        self._db = db
        self._collection_name = collection_name

    def find(self, key):
        tt_collection = self._db[self._collection_name]  # type: Collection
        res = tt_collection.find(key)
        return [TimeTable(None, e['subjects'], []) for e in res]
