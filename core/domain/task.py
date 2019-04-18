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


def task2dict(task: Task):
    return {
        'id': str(task.task_id),
        'subject': task.subject,
        'detail': task.detail,
        'deadline': task.deadline.isoformat(),
        'tags': task.tags
    }
