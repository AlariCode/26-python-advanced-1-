"""Демо модуль для курса"""

from dataclasses import dataclass, field
from datetime import datetime


@dataclass(order=True)
class Task:
    title: str
    secret_key: str = field(repr=False, compare=False)
    priority: int = 3
    done: bool = False
    created_at: datetime | None = None

    def __post_init__(self):
        if self.created_at is None:
            self.created_at = datetime.now()


task_1 = Task("Сделать лекцию", "mysecret")
task_2 = Task("Сделать лекцию", "mysecret")
print(task_1 == task_2)
print(task_1)
