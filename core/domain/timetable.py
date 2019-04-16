from datetime import date
from dataclasses import dataclass
from typing import List
from domain.timetablechange import TimeTableChange, timetable_change2dict


@dataclass
class TimeTable:
    date: date
    subjects: List[str]
    change: List[TimeTableChange]


def timetable2dict(timetable: TimeTable):
    return {
        'date': timetable.date.isoformat(),
        'subjects': timetable.subjects,
        'change': [timetable_change2dict(e) for e in timetable.change]
    }
