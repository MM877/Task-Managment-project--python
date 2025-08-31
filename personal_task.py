from task import Task

class PersonalTask(Task):
    def __init__(self, title, description, date, status, category):
        # Call the parent class (Task) to handle common fields
        super().__init__(title, description, date, status)

        # Save the category (extra info only for PersonalTask)
        self.category = category

    def save_to_dict(self):
        # Make a dictionary with all task information
        task_dict = {}
        task_dict["type"] = "PersonalTask"
        task_dict["title"] = self.title
        task_dict["description"] = self.description
        task_dict["date"] = self.date
        task_dict["status"] = self.status
        task_dict["category"] = self.category
        return task_dict

    def __str__(self):
        return "[Personal Task] " + self.title + " - Date: " + self.date + \
               " - Status: " + self.status + " - " + self.description + \
               " (Category: " + self.category + ")"
