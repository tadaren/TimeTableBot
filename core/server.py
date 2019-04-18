from bottle import *
import datetime

import config
from db import get_db
from domain.timetable import timetable2dict
from repository.eventrepository import EventRepository
from repository.taskrepository import TaskRepository
from repository.timetablechangerepository import TimeTableChangeRepository
from repository.timetablerepository import TimeTableRepository
from usecase.eventmanager import EventManager
from usecase.taskmanager import TaskManager
from usecase.timetablemanager import TimeTableManager

db = get_db('TimeTableBot')

timetable_repository = TimeTableRepository(db, config.TIMETABLE_COLLECTION_NAME)
timetable_change_repository = TimeTableChangeRepository(db, config.TIMETABLE_CHANGE_COLLECTION_NAME)
task_repository = TaskRepository(db, config.TASK_COLLECTION_NAME)
event_repository = EventRepository(db, config.EVENT_COLLECTION_NAME)

timetable_manager = TimeTableManager(timetable_repository, timetable_change_repository)
task_manager = TaskManager(task_repository)
event_manager = EventManager(event_repository)


@get('/timetable/get')
def timetable_get():
    date = datetime.date.fromisoformat(request.query.get('date'))
    timetable = timetable_manager.get(date)

    response.headers['Content-Type'] = 'application/json'
    if timetable is None:
        return {}
    return timetable2dict(timetable)


@post('/timetable/change')
def timetable_change():
    request_json = request.json
    timetable_manager.add(
        datetime.date.fromisoformat(request_json['date']),
        request_json['period'],
        request_json['subject'],
        request_json['tags']
    )


@get('/task/get')
def task_get():
    first_day = request.query.get('first_day')
    last_day = request.query.get('last_day')
    tags = request.query.getall('tags')
    if first_day is not None:
        first_day = datetime.date.fromisoformat(first_day)
    if last_day is not None:
        last_day = datetime.date.fromisoformat(last_day)

    tasks = task_manager.get(first_day, last_day, tags)

    response.headers['Content-Type'] = 'application/json'
    if not tasks:
        return {}
    return {'response': [task2dict(task) for task in tasks]}


run(host='0.0.0.0', port=80, debug=True, reloader=True)
