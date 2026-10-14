"""Вспомогательные функции приложения."""
from models import Task, Status


def filter_by_status(tasks: list[Task], status: Status) -> list[Task]:
    """Возвращает задачи с заданным статусом."""
    return [t for t in tasks if t.status == status]


def progress_percent(tasks: list[Task]) -> int:
    """Возвращает процент выполненных задач."""
    if not tasks:
        return 0
    done = len(filter_by_status(tasks, Status.DONE))
    return round(done * 100 / len(tasks))
