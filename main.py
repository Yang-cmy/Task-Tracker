import json
import os

from datetime import datetime

class TaskProperties:
    def __init__(self, id, description, status, created_at, updated_at):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return {
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

    @classmethod
    def from_dict(cls, data):
        return cls(
            data["id"],
            data["description"],
            data["status"],
            data["created_at"],
            data["updated_at"]
        )


def save_tasks(tasks):
    with open("Data.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)


def load_tasks():
    if not os.path.exists("Data.json"):
        return []

    try:
        with open("Data.json", "r", encoding="utf-8") as file:
            data = json.load(file)

    except json.JSONDecodeError:
        return []
    
    tasks = []

    for item in data:
        task = TaskProperties.from_dict(item)
        tasks.append(task)

    return tasks


def get_current_time():
    return datetime.now().isoformat(timespec = "seconds")

def add_task(description):
    tasks = load_tasks()

    if len(tasks) == 0:
        new_id = 1
    else:
        new_id = tasks[-1].id + 1

    now = get_current_time()

    new_task = TaskProperties(
        new_id,
        description,
        "todo",
        now,
        now
    )

    tasks.append(new_task)

    tasks_dict = []

    for task in tasks:
        tasks_dict.append(task.to_dict())

    save_tasks(tasks_dict)

    print(f"Task added successfully (ID: {new_id})")

def list_tasks(status = None):
    tasks = load_tasks()

    if len(tasks) == 0:
        print("No tasks found")
        return

    for task in tasks:
        if status is None or task.status == status:
            print(f"ID: {task.id} | {task.description} | Status: {task.status}")

def update_task(task_id,new_description):
    tasks = load_tasks()

    for task in tasks:
        if task.id == task_id:
            task.description = new_description
            task.updated_at = get_current_time()

            task_dict = []

            for item in tasks:
                task_dict.append(item.to_dict())

            save_tasks(task_dict)

            print(f"Task {task_id} updated succesfuly.")
            return

    print(f"Task with ID {task_id} not found.")

def delete_task(task_id):
    tasks = load_tasks()

    for task in tasks:
        if task.id == task_id:
            tasks.remove(task)

            task_dict = []

            for item in tasks:
                task_dict.append(item.to_dict())

            save_tasks(task_dict)

            print(f"Tasks {task_id} deleated succesfully.")
            return

    print(f"Task with ID {task_id} not found.")

list_tasks()