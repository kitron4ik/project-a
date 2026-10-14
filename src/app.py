"""Веб-интерфейс менеджера задач (Flask)."""
from datetime import datetime

from flask import Flask, render_template_string, request, redirect, url_for

from models import Task, Status
from utils import progress_percent
# функции из project-b (подключается подмодулем или пакетом)
from project_b_utils import (get_current_date, format_date, add_working_days,
                             capitalize_words, slugify, truncate)
from project_b_utils.file_utils import read_json, write_json
from project_b_utils.log_utils import get_logger

app = Flask(__name__)
log = get_logger("task-manager", log_file="app.log")
STORAGE = "instance/tasks.json"

TEMPLATE = """
<!doctype html><html lang=ru><meta charset=utf-8>
<title>Task Manager</title>
<style>
 body{font:15px/1.6 Segoe UI,Arial;margin:40px auto;max-width:720px;color:#1c2333}
 h1{font-size:24px;margin-bottom:4px} .meta{color:#6b7385}
 ul{padding-left:18px} li{padding:6px 0;border-bottom:1px solid #eee}
 .done{text-decoration:line-through;color:#6b7385}
 form{margin:18px 0} input{padding:8px;font:inherit;border:1px solid #dfe3ee;border-radius:6px}
 button{padding:9px 16px;font:inherit;background:#2f57c4;color:#fff;border:0;border-radius:6px}
</style>
<h1>Task Manager</h1>
<div class=meta>Дата: {{ today }} · выполнено {{ percent }}%</div>
<form method=post action="/add">
  <input name=title placeholder="Новая задача" size=40 required>
  <button>Добавить</button>
</form>
<ul>
{% for t in tasks %}
  <li class="{{ 'done' if t.status == 'done' else '' }}">
    {{ t.title }} <span class=meta>({{ t.slug }}, до {{ t.deadline }})</span>
  </li>
{% endfor %}
</ul>
"""


def load_tasks() -> list[dict]:
    return read_json(STORAGE).get("tasks", [])


def save_tasks(tasks: list[dict]) -> None:
    write_json(STORAGE, {"tasks": tasks})


@app.route("/")
def index():
    tasks = load_tasks()
    done = len([t for t in tasks if t["status"] == "done"])
    percent = round(done * 100 / len(tasks)) if tasks else 0
    log.info("Открыт список задач: %d шт.", len(tasks))
    return render_template_string(TEMPLATE, tasks=tasks,
                                  today=get_current_date(), percent=percent)


@app.route("/add", methods=["POST"])
def add():
    tasks = load_tasks()
    title = capitalize_words(request.form["title"])
    tasks.append({
        "id": len(tasks) + 1,
        "title": truncate(title, 60),
        "slug": slugify(title),
        "status": "todo",
        "deadline": format_date(add_working_days(datetime.now(), 3)),
    })
    save_tasks(tasks)
    log.info("Добавлена задача: %s", tasks[-1]["slug"])
    return redirect(url_for("index"))


if __name__ == "__main__":
    app.run(debug=True)
