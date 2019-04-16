from datetime import date
from dataclasses import dataclass
from typing import List


@dataclass
class TimeTableChange:
    time_table_change_id: str
    date: date
    period: int
    subject: str
    tags: List[str]


def timetable_change2dict(timetable_change: TimeTableChange):
    return {
        'id': str(timetable_change.time_table_change_id),
        'date': timetable_change.date.isoformat(),
        'period': timetable_change.period,
        'subject': timetable_change.subject,
        'tags': timetable_change.tags
    }
