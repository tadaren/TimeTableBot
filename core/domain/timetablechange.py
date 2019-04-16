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
