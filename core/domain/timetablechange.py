from datetime import date
from dataclasses import dataclass
from typing import List


@dataclass
class TimeTableChange:
    time_table_change_id: str
    date: date
    period: int
    subject: str
    tag: List[str]


def timetable_change2dict(timetable_change: TimeTableChange):
    return {
        'id': timetable_change.time_table_change_id,
        'date': timetable_change.date.isoformat(),
        'period': timetable_change.period,
        'subject': timetable_change.subject,
        'tag': timetable_change.tag
    }
