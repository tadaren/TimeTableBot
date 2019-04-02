from datetime import date
from dataclasses import dataclass
from typing import List
from domain.timetablechange import TimeTableChange


@dataclass
class TimeTable:
    date: date
    subjects: List[str]
    change: List[TimeTableChange]
