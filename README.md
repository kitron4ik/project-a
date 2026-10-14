# project-a (Task Manager)

Веб-приложение для управления задачами. Использует библиотеку
**project-b-utils** для работы с датами и строками.

## Способы подключения библиотеки

1. **Git Submodule** — каталог `libs/project-b`, ветка `main`.
2. **Git Subtree** — ветка `feature/subtree-approach`.
3. **Пакетный менеджер** — `pip install -e ../project-b`.

## Запуск

```bash
git clone --recurse-submodules <url>
pip install -r requirements.txt
python src/main.py
```

## Тесты

```bash
pytest tests/
```
