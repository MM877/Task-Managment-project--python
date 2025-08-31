from task import Task

class WorkTask(Task):
    def __init__(self, title, description, date, status, priority):
        # Call the parent class (Task) to handle common fields
        super().__init__(title, description, date, status)

        # Save the priority (extra info only for WorkTask)
        self.priority = priority

    def save_to_dict(self):
        # Make a dictionary with all task information
        task_dict = {}
        task_dict["type"] = "WorkTask"
        task_dict["title"] = self.title
        task_dict["description"] = self.description
        task_dict["date"] = self.date
        task_dict["status"] = self.status
        task_dict["priority"] = self.priority
        return task_dict

    def __str__(self):
        return "[Work Task] " + self.title + " - Date: " + self.date + \
               " - Status: " + self.status + " - " + self.description + \
               " (Priority: " + self.priority + ")"
