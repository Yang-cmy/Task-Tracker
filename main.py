import json

class TaskProperties:
    def __init__(self, id, description, status, created_at, updated_at):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return{
            "id": self.id,
            "description": self.description,
            "status": self.status,
            "created_at": self.created_at,
            "updated_at": self.updated_at
        }

def save_tasks(tasks):
    with open("Data.json", "w", encoding="utf-8") as file:
        json.dump(tasks, file, indent=4)

def load_tasks():
    with open("Data.json", "r", encoding="utf-8") as file:
        tasks = json.load(file)

        return tasks


task1 = TaskProperties(
    1,
    "Study Python",
    "todo",
    "2026-09-25",
    "2026-09-25"
)

task2 = TaskProperties(
    2,
    "Go shopping",
    "todo",
    "2026-09-25",
    "2026-09-25"
)


tasks = [task1.to_dict(), task2.to_dict()]


save_tasks(tasks)

loaded_tasks = load_tasks()

print(loaded_tasks[1])
        