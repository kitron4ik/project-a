"""Модели предметной области менеджера задач."""
from dataclasses import dataclass, field
from datetime import datetime
from enum import Enum


class Status(str, Enum):
    TODO = "todo"
    IN_PROGRESS = "in_progress"
    DONE = "done"


@dataclass
class Task:
    """Задача менеджера задач."""
    task_id: int
    title: str
    description: str = ""
    status: Status = Status.TODO
    created_at: datetime = field(default_factory=datetime.now)
    deadline: datetime | None = None

    def complete(self) -> None:
        self.status = Status.DONE

    def is_overdue(self) -> bool:
        return (self.deadline is not None
                and self.status != Status.DONE
                and self.deadline < datetime.now())
