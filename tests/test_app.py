"""Тесты веб-интерфейса Task Manager (Flask test client)."""
import app as task_app


def make_client(tmp_path, monkeypatch):
    monkeypatch.setattr(task_app, "STORAGE", str(tmp_path / "tasks.json"))
    return task_app.app.test_client()


def test_index_empty(tmp_path, monkeypatch):
    client = make_client(tmp_path, monkeypatch)
    response = client.get("/")
    assert response.status_code == 200
    assert "Task Manager" in response.get_data(as_text=True)


def test_add_task_uses_library(tmp_path, monkeypatch):
    client = make_client(tmp_path, monkeypatch)
    response = client.post("/add", data={"title": "подготовить отчёт по git"},
                           follow_redirects=True)
    html = response.get_data(as_text=True)
    assert "Подготовить Отчёт По Git" in html          # capitalize_words
    assert "подготовить-отчёт-по-git" in html           # slugify
    assert task_app.load_tasks()[0]["status"] == "todo"  # write_json / read_json
