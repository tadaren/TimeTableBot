import datetime
from typing import List
import bson

from domain.task import Task
from util import build_date_query


class TaskManager:
    def __init__(self, repository):
        self.repository = repository

    def get(self, first_day: datetime.date = None, last_day: datetime.date = None, tags: List[str] = []):
        query = {}
        date_query = build_date_query(first_day, last_day)
        if date_query:
            query['date'] = date_query
        if tags:
            query['tag'] = {'$all': tags}
        ret = self.repository.find(query)
        return ret

    def update(self, task_id, subject, detail, deadline, tag):
        self.repository.update({'_id': bson.ObjectId(task_id)}, Task(task_id, subject, detail, deadline, tag))

    def delete(self, task_id):
        self.repository.delete({'_id': bson.ObjectId(task_id)})

    def add(self, subject, detail, deadline, tag):
        self.repository.insert(Task('', subject, detail, deadline, tag))
