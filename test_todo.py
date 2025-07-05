import os
import json
import todo

# 🧹 Helper: Clear tasks.json before each test
def setup():
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")
    todo.clear_tasks()

# ✅ Test adding and listing tasks
def test_add_and_list():
    setup()
    todo.add_task("Buy groceries")
    todo.add_task("Read book")

    tasks = todo.load_tasks()
    assert len(tasks) == 2
    assert tasks[0]["task"] == "Buy groceries"
    assert tasks[1]["task"] == "Read book"

# ✅ Test completing a task
def test_complete_task():
    setup()
    todo.add_task("Incomplete task")
    todo.complete_task(0)

    tasks = todo.load_tasks()
    assert tasks[0]["done"] is True

# ✅ Test deleting a task
def test_delete_task():
    setup()
    todo.add_task("Keep this")
    todo.add_task("Delete this")

    todo.delete_task(1)
    tasks = todo.load_tasks()
    assert len(tasks) == 1
    assert tasks[0]["task"] == "Keep this"

# ✅ Test editing a task
def test_edit_task():
    setup()
    todo.add_task("Wrong title")
    todo.edit_task(0, "Fixed title")

    tasks = todo.load_tasks()
    assert tasks[0]["task"] == "Fixed title"

# ✅ Test searching for tasks
def test_search_tasks():
    setup()
    todo.add_task("Write Python code")
    todo.add_task("Do laundry")

    results = todo.search_tasks("python")
    assert len(results) == 1
    assert results[0]["task"] == "Write Python code"

# ✅ Test listing completed/incomplete
def test_completed_and_incomplete_lists():
    setup()
    todo.add_task("Task A")
    todo.add_task("Task B")
    todo.complete_task(0)

    completed = todo.list_completed()
    incomplete = todo.list_incomplete()

    assert len(completed) == 1
    assert len(incomplete) == 1
    assert completed[0]["task"] == "Task A"
    assert incomplete[0]["task"] == "Task B"

# ✅ Test clearing tasks
def test_clear_tasks():
    setup()
    todo.add_task("A")
    todo.add_task("B")
    todo.clear_tasks()

    tasks = todo.load_tasks()
    assert tasks == []

# ✅ Test adding with due date
def test_add_task_with_due_date():
    setup()
    todo.add_task("Submit report", due_date="2025-07-01")

    tasks = todo.load_tasks()
    assert tasks[0]["task"] == "Submit report"
    assert tasks[0]["due"] == "2025-07-01"