class Task:
    def __init__(self, title, description, date, status):
        self.title = title
        self.description = description
        self.date = date
        self.status = status

    def save_to_dict(self):
        # Make a dictionary with all task information
        task_dict = {}
        task_dict["type"] = "Task"
        task_dict["title"] = self.title
        task_dict["description"] = self.description
        task_dict["date"] = self.date
        task_dict["status"] = self.status
        return task_dict

    def __str__(self):
        return "[Task] " + self.title + " - Date: " + self.date + \
               " - Status: " + self.status + " - " + self.description
