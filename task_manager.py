import json
import os
from prettytable import PrettyTable
from datetime import datetime
from colorama import Fore, Style, init
init(autoreset=True)
from personal_task import PersonalTask
from work_task import WorkTask
from task import Task


class TaskManager:
    def __init__(self, filename="tasks.json"):
        self.tasks = []
        self.filename = filename
        self.load_from_json()  # Load tasks when the program starts

    # -------- Save tasks to JSON --------
    def save_to_json(self):
        try:
            # Open file for writing
            with open(self.filename, "w") as f:
                tasks_list = []  # make a list to store dictionaries

                # Loop through tasks and convert each one to dictionary
                for task in self.tasks:
                    task_dict = task.save_to_dict()
                    tasks_list.append(task_dict)

                # Save the list of task dictionaries to JSON
                json.dump(tasks_list, f, indent=2)

            print("Tasks have been saved successfully!")
        except Exception as e:
            print("Error while saving tasks:", e)

    # -------- Load tasks from JSON --------
    def load_from_json(self):
        if not os.path.exists(self.filename):
            self.tasks = []
            return

        try:
            with open(self.filename, "r") as f:
                data = json.load(f)

            # Clear old tasks
            self.tasks = []

            for task_dict in data:
                if task_dict["type"] == "PersonalTask":
                    task = PersonalTask(
                        task_dict["title"],
                        task_dict["description"],
                        task_dict["date"],
                        task_dict["status"],
                        task_dict["category"]
                    )
                elif task_dict["type"] == "WorkTask":
                    task = WorkTask(
                        task_dict["title"],
                        task_dict["description"],
                        task_dict["date"],
                        task_dict["status"],
                        task_dict["priority"]
                    )
                else:
                    task = Task(
                        task_dict["title"],
                        task_dict["description"],
                        task_dict["date"],
                        task_dict["status"]
                    )

                self.tasks.append(task)

        except Exception as e:
            print(Fore.RED + "Error while Loading tasks:" + str(e) + Style.RESET_ALL)
            self.tasks = []

    # -------- Add a new task --------
    from datetime import datetime

    def add(self):
        
        print(Fore.CYAN + "\nWhat kind of task do you want to add?" + Style.RESET_ALL)
        print(Fore.YELLOW + "1 - Personal Task")
        print(Fore.YELLOW + "2 - Work Task")

        choice = input("Enter choice (1 or 2): ")

        # Common fields
        title = input("Enter Title: ")
        description = input("Enter Description: ")

        # --- DATE INPUT with validation ---
        while True:
            date_input = input("Enter Task Date (YYYY-MM-DD): ")
            try:
                # try to convert to real date
                datetime.strptime(date_input, "%Y-%m-%d")
                date = date_input   # valid format
                break
            except ValueError:
                print(Fore.RED + "Invalid date format! Please use YYYY-MM-DD (Example: 2025-08-25)" + Style.RESET_ALL)


        # Status
        print(Fore.MAGENTA + "Choose Status:")
        print(Fore.GREEN + "1 - Incomplete")
        print(Fore.RED + "2 - Complete")
        print(Fore.BLUE + "3 - In Progress")
        status_choice = input("Enter choice: ")

        if status_choice == "2":
            status = "complete"
        elif status_choice == "3":
            status = "in progress"
        else:
            status = "incomplete"

        # Personal Task
        if choice == "1":
            print("\nChoose a Category:")
            print("1 - Health")
            print("2 - Family")
            print("3 - Hobby")
            print("4 - Study")
            print("5 - Other")

            cat_choice = input("Enter choice (1-5): ")

            if cat_choice == "1":
                category = "Health"
            elif cat_choice == "2":
                category = "Family"
            elif cat_choice == "3":
                category = "Hobby"
            elif cat_choice == "4":
                category = "Study"
            else:
                category = "Other"

            task = PersonalTask(title, description, date, status, category)

        # Work Task
        elif choice == "2":
            print("\nChoose Priority:")
            print("1 - High")
            print("2 - Medium")
            print("3 - Low")

            p_choice = input("Enter choice: ")

            if p_choice == "1":
                priority = "High"
            elif p_choice == "2":
                priority = "Medium"
            else:
                priority = "Low"

            task = WorkTask(title, description, date, status, priority)

        # Normal Task
        else:
            task = Task(title, description, date, status)

        # Add to list and save
        self.tasks.append(task)
        self.save_to_json()
        print(Fore.GREEN + " Task Added!\n" + Style.RESET_ALL)

    #------NA COLOR FUNCTION-----
    def color_na(self,value):
        if value == "N/A":
            return Fore.RED + value + Style.RESET_ALL
        return value

    # -------- Read all tasks --------
    def read(self):
        # Check if we have any tasks
        
        if len(self.tasks) == 0:
            print(Fore.RED+"No Tasks Yet. Go and Add Task\n")
            return

        # Create a new pretty table
        self.table = PrettyTable()
        
        # Set up column headers (what shows at the top of each column)
        self.table.field_names = ["#", "Title", "Description", "Date", "Status", "Type", "Priority", "Category"]
        
        # Go through each task one by one
        for idx, task in enumerate(self.tasks, start=1):
            # Convert task object to dictionary so we can easily get its data
            set_task_attr = task.save_to_dict()
            
            # Get the basic information that all tasks have
            title = self.color_na(set_task_attr.get("title", "N/A"))
            description = self.color_na(set_task_attr.get("description", "N/A"))
            date = self.color_na(set_task_attr.get("date", "N/A"))
            status = self.color_na(set_task_attr.get("status", "N/A"))
            task_type = set_task_attr.get("type", "Task")

            # Check what type of task this is and get the right extra info
            if task_type == "WorkTask":
                priority = self.color_na(set_task_attr.get("priority", "N/A"))  # Work tasks have priority
                category = self.color_na("N/A")  # Work tasks don't have category
            elif task_type == "PersonalTask":
                priority = self.color_na("N/A")  # Personal tasks don't have priority
                category = self.color_na(set_task_attr.get("category", "N/A"))  # Personal tasks have category
            else:
                priority = self.color_na("N/A")  # Regular tasks don't have either
                category = self.color_na("N/A")
                        
            # Add this task's information as a new row in the table
            self.table.add_row([
                idx,                    # Task number (1, 2, 3 )
                title,                  # Task title
                description,            # Task description
                date,                   # Task date
                status.title(),         # Task status (capitalize first letter)
                task_type,              # What type of task it is
                priority,               # Priority (only for work tasks)
                category                # Category (only for personal tasks)
            ])
        
        # Make the table look better
        self.table.align = "l"          # Align text to the left
        self.table.max_width = 20       # Don't let columns get too wide
        
        # Show the table
        print(self.table)

    # -------- Delete a task --------
    def delete(self):
        self.read()
        if len(self.tasks) == 0:
            return

        try:
            choice = int(input("Enter Task Number to Delete: "))
            if choice > 0 and choice <= len(self.tasks):
                confirm = input("Are you sure you want to delete it? (yes/no): ").lower()
                if confirm == "yes":
                    deleted = self.tasks.pop(choice - 1)
                    self.save_to_json()
                    print(f"Deleted Task: {deleted}\n")
            else:
                print("Invalid Task Number!\n")
        except ValueError:
            print(Fore.RED+"No Tasks Yet. Go and Add Task\n")

    # -------- Update a task --------
        # -------- Update a task --------
    def update(self):
        self.read()
        if len(self.tasks) == 0:
            return

        try:
            choice = int(input("Enter task number to update: "))
            if choice > 0 and choice <= len(self.tasks):
                old_task = self.tasks[choice - 1]
                print(f"\nEditing: {old_task}\n")

                # Title & Description
                new_title = input("New Title: ")
                new_description = input("New Description: ")

                # --- DATE INPUT with validation ---
                while True:
                    date_input = input("Enter New Date (YYYY-MM-DD): ")
                    try:
                        datetime.strptime(date_input, "%Y-%m-%d")  # validate
                        new_date = date_input
                        break
                    except ValueError:
                        print(Fore.RED+" Invalid date format! Please use YYYY-MM-DD (Example: 2025-08-25)")

                # --- Status choices ---
                print("Choose New Status:")
                print("1 - Incomplete")
                print("2 - Complete")
                print("3 - In Progress")
                status_choice = input("Enter choice: ")

                if status_choice == "2":
                    new_status = "complete"
                elif status_choice == "3":
                    new_status = "in progress"
                else:
                    new_status = "incomplete"

                # --- Handle task type ---
                task_type = old_task.save_to_dict()["type"]

                if task_type == "PersonalTask":
                    new_category = input("New Category: ")
                    self.tasks[choice - 1] = PersonalTask(
                        new_title, new_description, new_date, new_status, new_category
                    )

                elif task_type == "WorkTask":
                    print("Priority Options: 1-High  2-Medium  3-Low")
                    priority_choice = input("Choose Priority: ")

                    if priority_choice == "1":
                        priority = Fore.RED + "High" + Style.RESET_ALL
                    elif priority_choice == "2":
                        priority = Fore.YELLOW + "Medium" + Style.RESET_ALL
                    else:
                        priority = Fore.GREEN + "Low" + Style.RESET_ALL

                    self.tasks[choice - 1] = WorkTask(
                        new_title, new_description, new_date, new_status, priority
                    )

                else:
                    self.tasks[choice - 1] = Task(
                        new_title, new_description, new_date, new_status
                    )

                self.save_to_json()
                print("Task Updated!\n")

            else:
                print(Fore.RED+"Invalid number!\n")

        except ValueError:
            print(Fore.RED+"Please enter a valid number!\n")


         # -------- Update only the status of a task --------
    def task_status(self):
        self.read()
        if len(self.tasks) == 0:
            return

        try:
            choice = int(input("Enter task number to update status: "))
            if choice > 0 and choice <= len(self.tasks):
                task = self.tasks[choice - 1]

                print("\nChoose New Status:")
                print(Fore.RED+"1 - Incomplete")
                print(Fore.GREEN+"2 - Complete")
                print(Fore.BLUE+"3 - In Progress")

                status_choice = input("Enter choice: ")

                if status_choice == "2":
                    new_status = "complete"
                elif status_choice == "3":
                    new_status = "in progress"
                else:
                    new_status = "incomplete"

                # update the task
                task.status = new_status
                self.save_to_json()
                print(Fore.GREEN + f"Status of '{task.title}' updated to {task.status}\n" + Style.RESET_ALL)

            else:
                print(Fore.RED + "Invalid number!\n")

        except ValueError:
            print(Fore.RED + "Please enter a valid number!\n")

    def sorting_tasks(self):
        print(Fore.MAGENTA+"Sort by: ")
        print(Fore.RED +"1 - date")
        print(Fore.GREEN+"2 - task name")
        print(Fore.BLUE+ "3 - status")
        sor= input(Fore.LIGHTCYAN_EX+ "-> ")

        if sor == "1":
            self.tasks = sorted(self.tasks, key=lambda task: task.date, reverse=True)
            print(self.read())
        elif sor == "2":
            self.tasks = sorted(self.tasks, key=lambda task: task.title)
            print(self.read())
        elif sor == "3":
            status_order = {"completed": 1, "in progress": 2, "incomplete": 3}
            self.tasks = sorted(self.tasks, key=lambda task: status_order.get(task.status, 1))
            print(self.read())
        else:
            print("invalid choice!\n")

