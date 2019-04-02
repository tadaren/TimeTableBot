import datetime
from dataclasses import dataclass
from typing import List
from domain.timetablechange import TimeTableChange


@dataclass
class TimeTable:
    date: datetime
    subjects: List[str]
    change: List[TimeTableChange]
