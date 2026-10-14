"""Утилиты для работы с датами."""
from datetime import datetime, timedelta

DEFAULT_FORMAT = "%d.%m.%Y"


def get_current_date(fmt: str = DEFAULT_FORMAT) -> str:
    """Возвращает текущую дату в виде строки."""
    return datetime.now().strftime(fmt)


def format_date(value: datetime, fmt: str = DEFAULT_FORMAT) -> str:
    """Форматирует дату по заданному шаблону."""
    if not isinstance(value, datetime):
        raise TypeError("Ожидается объект datetime")
    return value.strftime(fmt)


def days_between(start: datetime, end: datetime) -> int:
    """Возвращает количество дней между двумя датами."""
    return abs((end - start).days)


def add_working_days(start: datetime, days: int) -> datetime:
    """Прибавляет к дате заданное число рабочих дней (без выходных)."""
    current = start
    added = 0
    while added < days:
        current += timedelta(days=1)
        if current.weekday() < 5:
            added += 1
    return current


def is_weekend(value: datetime) -> bool:
    """Возвращает True, если дата приходится на субботу или воскресенье."""
    return value.weekday() >= 5


def start_of_month(value: datetime) -> datetime:
    """Возвращает первое число месяца для переданной даты."""
    return value.replace(day=1, hour=0, minute=0, second=0, microsecond=0)
