"""Точка входа приложения Task Manager."""
from datetime import datetime, timedelta

# функции библиотеки project-b-utils, установленной как пакет
from project_b_utils import get_current_date, reverse_string

from models import Task, Status
from utils import filter_by_status, progress_percent


def build_demo_tasks() -> list[Task]:
    return [
        Task(1, "Подготовить отчёт по лабораторной работе",
             deadline=datetime.now() + timedelta(days=2)),
        Task(2, "Настроить подмодуль project-b", status=Status.IN_PROGRESS),
        Task(3, "Написать тесты интеграции", status=Status.DONE),
    ]


def main() -> None:
    tasks = build_demo_tasks()
    print("=== Task Manager ===")
    print(f"Дата: {get_current_date()}")
    print(f"Заголовок наоборот: {reverse_string('Task Manager')}")
    for task in tasks:
        mark = "x" if task.status == Status.DONE else " "
        print(f"[{mark}] {task.task_id}. {task.title} ({task.status.value})")
    print(f"Выполнено: {progress_percent(tasks)}%")


if __name__ == "__main__":
    main()
