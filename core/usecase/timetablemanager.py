import datetime
from typing import List

from domain.timetablechange import TimeTableChange


class TimeTableManager:
    def __init__(self, timetable_repository, timetable_change_repository):
        self.tt_repository = timetable_repository
        self.ttc_repository = timetable_change_repository

    def get(self, date: datetime.date):
        timetable = self.tt_repository.find({'date': date.isoformat()})
        if not timetable:
            return None

        timetable = timetable[0]
        timetable_change = self.ttc_repository.find({'date': date.isoformat()})
        timetable.change = timetable_change
        return timetable

    def add(self, date: datetime.date, period: int, subject: str, tags: List[str]):
        self.ttc_repository.insert(TimeTableChange('', date, period, subject, tags))
