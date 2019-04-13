import datetime

import bson
from pymongo.collection import Collection

from domain.task import Task


class TaskRepository:
    def __init__(self, db, collection_name):
        self._db = db
        self._collection_name = collection_name

    def insert(self, task: Task):
        task_collection = self._db[self._collection_name]  # type: Collection
        task_dict = task2dict(task)
        task_collection.insert_one(task_dict)

    def find(self, key):
        task_collection = self._db[self._collection_name]  # type: Collection
        res = task_collection.find(key)
        task_list = [dict2task(e) for e in res]
        return task_list

    def delete(self, key):
        task_collection = self._db[self._collection_name]  # type: Collection
        task_collection.delete_one(key)

    def update(self, key, task: Task):
        task_collection = self._db[self._collection_name]  # type: Collection
        task_collection.update_one(key, task2dict(task))


def task2dict(task: Task):
    if task.task_id:
        return {
            '_id': bson.ObjectId(task.task_id),
            'subject': task.subject,
            'detail': task.detail,
            'deadline': task.deadline.isoformat(),
            'tag': task.tag
        }
    return {
        'subject': task.subject,
        'detail': task.detail,
        'deadline': task.deadline.isoformat(),
        'tag': task.tag
    }


def dict2task(obj):
    return Task(
        str(obj['_id']),
        obj['subject'],
        obj['detail'],
        datetime.date.fromisoformat(obj['deadline']),
        obj['tag']
    )
