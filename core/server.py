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


run(host='0.0.0.0', port=80, debug=True, reloader=True)
