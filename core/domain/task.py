from datetime import date
from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    task_id: int
    subject: str
    detail: str
    deadline: date
    tag: List[str]

