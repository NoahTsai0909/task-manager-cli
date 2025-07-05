import json
import os

DATA_FILE = "tasks.json"


def load_tasks():
    if not os.path.exists(DATA_FILE):
        return []
    try:
        with open(DATA_FILE, "r") as f:
            return json.load(f)
    except json.JSONDecodeError:
        print("⚠️ Warning: Corrupted task file. Starting fresh.")
        return []


def save_tasks(tasks):
    with open(DATA_FILE, "w") as f:
        json.dump(tasks, f, indent=2)


def add_task(task, due_date=None):
    tasks = load_tasks()
    tasks.append({"task": task, "done": False, "due": due_date})
    save_tasks(tasks)


def delete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        del tasks[index]
        save_tasks(tasks)


def edit_task(index, new_text):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["task"] = new_text
        save_tasks(tasks)


def search_tasks(keyword):
    tasks = load_tasks()
    return [t for t in tasks if keyword.lower() in t["task"].lower()]


def list_tasks():
    tasks = load_tasks()
    for i, t in enumerate(tasks):
        status = "Y" if t["done"] else "N"
        print(f"{i+1}. [{status}] {t['task']}")


def list_completed():
    return [t for t in load_tasks() if t["done"]]


def list_incomplete():
    return [t for t in load_tasks() if not t["done"]]


def export_tasks(filename="export.json"):
    tasks = load_tasks()
    with open(filename, "w") as f:
        json.dump(tasks, f, indent=2)


def clear_tasks():
    save_tasks([])


def complete_task(index):
    tasks = load_tasks()
    if 0 <= index < len(tasks):
        tasks[index]["done"] = True
        save_tasks(tasks)


# CLI example
if __name__ == "__main__":
    import sys

    if len(sys.argv) < 2:
        print("Usage: python todo.py [add/list/complete/delete/edit/search]")
    elif sys.argv[1] == "add":
        add_task(" ".join(sys.argv[2:]))
    elif sys.argv[1] == "list":
        list_tasks()
    elif sys.argv[1] == "complete":
        complete_task(int(sys.argv[2]) - 1)
    elif sys.argv[1] == "delete":
        delete_task(int(sys.argv[2]) - 1)
    elif sys.argv[1] == "edit":
        index = int(sys.argv[2]) - 1
        new_text = " ".join(sys.argv[3:])
        edit_task(index, new_text)
    elif sys.argv[1] == "search":
        results = search_tasks(" ".join(sys.argv[2:]))
        for i, t in enumerate(results):
            status = "Y" if t["done"] else "N"
            print(f"{i+1}. [{status}] {t['task']}")
