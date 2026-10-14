# project-b-utils

Библиотека утилит для работы с датами и строками. Используется как зависимость
в проекте **project-a (Task Manager)**.

## Установка

```bash
pip install -e .
```

## Состав

| Модуль | Функции |
|---|---|
| `date_utils` | `get_current_date`, `format_date`, `days_between`, `add_working_days` |
| `string_utils` | `reverse_string`, `capitalize_words`, `slugify`, `truncate` |

## Запуск тестов

```bash
pytest tests/
```
