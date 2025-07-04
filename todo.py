import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    with open(DATA_FILE, "r") as f:
        return json.load(f)


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f)


def add_task(task):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)


def list_tasks():
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        status = "Y" if t["done"] else "N"
        print(f"{i+1}. [{status}] {t['task']}")


def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)


# CLI example
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python todo.py [add/list/complete] [task/index]")
    elif sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "complete":
        complete_task(int(sys.argv[2]) - 1)
