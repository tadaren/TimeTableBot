import datetime
from dataclasses import dataclass
from typing import List


@dataclass
class TimeTableChange:
    time_table_change_id: int
    date: datetime
    period: int
    subject: str
    tag: List[str]
