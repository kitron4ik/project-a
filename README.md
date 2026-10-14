# project-a (Task Manager)

Веб-приложение для управления задачами на Flask. Использует библиотеку
**project-b-utils** ([project-b](../project-b)) для работы с датами, строками,
файлами и логированием.

## Структура

```
project-a/
├── src/
│   ├── app.py              # веб-интерфейс (Flask)
│   ├── main.py             # консольная версия
│   ├── models.py           # Task, Status
│   ├── utils.py            # фильтрация и статистика
│   └── module_loader.py    # подключение библиотеки через подмодуль
├── libs/project-b/         # подмодуль (git submodule)
├── tests/                  # тесты приложения и интеграции
├── requirements.txt
└── .github/                # CI, автообновление подмодуля, Dependabot
```

## Способы подключения библиотеки project-b

| Способ | Где | Как подключается |
|---|---|---|
| Git Submodule | ветка `main`, каталог `libs/project-b` | `git submodule add`, затем `sys.path` (см. `module_loader.py`) |
| Git Subtree | ветка `feature/subtree-approach` | `git subtree add --prefix=libs/project-b ... --squash` |
| Пакетный менеджер | `requirements.txt` | `-e ../project-b` -> `from project_b_utils import ...` |

В приложении используется **пакетный менеджер**; подмодуль хранит зафиксированную
версию исходников библиотеки и обновляется автоматически (см. `.github/`).

## Установка и запуск

```bash
git clone --recurse-submodules <url> project-a
cd project-a
python -m venv .venv && source .venv/Scripts/activate
pip install -r requirements.txt       # ставит project-b-utils из ../project-b
python src/app.py                     # http://127.0.0.1:5000
```

Консольная версия: `python src/main.py`.

## Тесты

```bash
pytest tests/ -v
```
