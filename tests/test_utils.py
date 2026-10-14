"""Тесты библиотеки утилит."""
from datetime import datetime

from date_utils import (get_current_date, format_date, days_between, add_working_days,
                        is_weekend, start_of_month)
from string_utils import (reverse_string, capitalize_words, slugify, truncate,
                          count_words, is_palindrome)


def test_get_current_date_format():
    assert len(get_current_date()) == 10


def test_format_date():
    assert format_date(datetime(2026, 9, 30)) == "30.09.2026"


def test_days_between():
    assert days_between(datetime(2026, 9, 1), datetime(2026, 9, 30)) == 29


def test_add_working_days():
    # 30.09.2026 — среда, +3 рабочих дня = понедельник 05.10.2026
    assert add_working_days(datetime(2026, 9, 30), 3) == datetime(2026, 10, 5)


def test_reverse_string():
    assert reverse_string("Hello") == "olleH"


def test_capitalize_words():
    assert capitalize_words("hello world") == "Hello World"


def test_slugify():
    assert slugify("Управление задачами  v2") == "управление-задачами-v2"


def test_truncate():
    assert truncate("abcdefgh", 5) == "abcd…"


def test_is_weekend():
    assert is_weekend(datetime(2026, 10, 10)) is True    # суббота
    assert is_weekend(datetime(2026, 10, 12)) is False   # понедельник


def test_start_of_month():
    assert start_of_month(datetime(2026, 10, 14, 15, 30)) == datetime(2026, 10, 1)


def test_count_words():
    assert count_words("менеджер задач на Flask") == 4


def test_is_palindrome():
    assert is_palindrome("А роза упала на лапу Азора") is True
    assert is_palindrome("project") is False
