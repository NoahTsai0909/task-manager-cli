import os
import todo

def test_add_and_list():
    # Remove existing tasks file
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")

    todo.add_task("Test Task 1")
    todo.add_task("Test Task 2")
    tasks = todo.load_tasks()
    assert tasks[0]["task"] == "Test Task 1"
    assert tasks[1]["task"] == "Test Task 2"

def test_complete_task():
    if os.path.exists("tasks.json"):
        os.remove("tasks.json")
    todo.add_task("Incomplete Task")
    todo.complete_task(0)
    tasks = todo.load_tasks()
    assert tasks[0]["done"] == True