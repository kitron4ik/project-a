"""Тесты приложения Task Manager."""
from datetime import datetime, timedelta

from models import Task, Status
from utils import filter_by_status, progress_percent


def test_complete_task():
    task = Task(1, "Тестовая задача")
    task.complete()
    assert task.status == Status.DONE


def test_is_overdue():
    overdue = Task(2, "Просроченная", deadline=datetime.now() - timedelta(days=1))
    assert overdue.is_overdue() is True


def test_filter_by_status():
    tasks = [Task(1, "A"), Task(2, "B", status=Status.DONE)]
    assert len(filter_by_status(tasks, Status.DONE)) == 1


def test_progress_percent():
    tasks = [Task(1, "A", status=Status.DONE), Task(2, "B")]
    assert progress_percent(tasks) == 50
