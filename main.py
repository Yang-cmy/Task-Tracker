class TaskProperties:
    def __init__(self, id, description, status, created_at, updated_at):
        self.id = id
        self.description = description
        self.status = status
        self.created_at = created_at
        self.updated_at = updated_at

    def to_dict(self):
        return{
            "id \n": self.id,
            "description \n": self.description,
            "status \n": self.status,
            "created_at \n": self.created_at,
            "updated_at \n": self.updated_at
        }


task1 = TaskProperties(
    1,
    "Study Python",
    "todo",
    "2026-09-25",
    "2026-09-25"
)

print(task1.to_dict())
        