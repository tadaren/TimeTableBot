from datetime import date
from dataclasses import dataclass
from typing import List


@dataclass
class Task:
    task_id: str
    subject: str
    detail: str
    deadline: date
    tags: List[str]

