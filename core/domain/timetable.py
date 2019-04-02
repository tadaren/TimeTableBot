import datetime
from dataclasses import dataclass
from typing import List
from core.domain import TimeTableChange


@dataclass
class TimeTable:
    date: datetime
    subjects: List[str]
    change: List[TimeTableChange]
