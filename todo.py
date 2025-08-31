from task_manager import TaskManager
from colorama import Fore, Style , init

# Initialize colorama
init(autoreset=True)

class ToDo:
    def __init__(self):
        self.manager = TaskManager()
        self.menu()

    def menu(self):
        while True:
            print("\n" + "="*50)
            print(Fore.CYAN + "\nWELCOME TO YOUR TODO\n")

            choice = input(f"""{Fore.YELLOW}Select an option:
{Fore.GREEN}    1 - Add Task
{Fore.BLUE}    2 - Read Tasks
{Fore.MAGENTA}    3 - Update Task
{Fore.RED}    4 - Delete Task
{Fore.LIGHTGREEN_EX}    5 - Change Task Status 
{Fore.BLUE}    6 - Sorting Tasks
{Fore.CYAN}    7 - Exit  
{Fore.WHITE}-> {Style.RESET_ALL}""")

            if choice == "1":
                self.manager.add()
            elif choice == "2":
                self.manager.read()
            elif choice == "3":
                self.manager.update()
            elif choice == "4":
                self.manager.delete()
            elif choice == "5":
                self.manager.task_status()
            elif choice == "6":
                self.manager.sorting_tasks()
            elif choice == "7":
                print(Fore.GREEN + "Goodbye!")
                break
            else:
                print(Fore.RED + "Invalid choice, try again.\n")

if __name__ == "__main__":
    ToDo()
