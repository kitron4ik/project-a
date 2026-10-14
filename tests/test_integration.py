"""Тесты интеграции project-a с библиотекой project-b."""
from datetime import datetime

from project_b_utils import format_date, capitalize_words, slugify
from project_b_utils.file_utils import read_json, write_json
from project_b_utils.log_utils import get_logger


def test_library_is_available():
    assert format_date(datetime(2026, 9, 30)) == "30.09.2026"


def test_title_normalization():
    title = capitalize_words("настроить подмодуль project b")
    assert title == "Настроить Подмодуль Project B"
    assert slugify(title) == "настроить-подмодуль-project-b"


def test_storage_roundtrip(tmp_path):
    path = tmp_path / "tasks.json"
    write_json(str(path), {"tasks": [{"id": 1, "title": "Задача"}]})
    assert read_json(str(path))["tasks"][0]["title"] == "Задача"


def test_logger_created():
    log = get_logger("test-logger")
    assert log.handlers
