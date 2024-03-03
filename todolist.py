from datetime import datetime

class Task:
    def __init__(self, description, date, time):
        self.description = description
        self.date = date
        self.time = time

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        if any(t.date == task.date and t.time == task.time for t in self.tasks):
            print("A task already exists at that date and time.")
        else:
            self.tasks.append(task)
            date_str = task.date.strftime("%Y-%m-%d")
            time_str = task.time.strftime("%H:%M")
            print(f"Task '{task.description}' on {date_str} at {time_str} added.")

    def remove_task(self, task_description):
        for task in self.tasks:
            if task.description == task_description:
                self.tasks.remove(task)
                print(f"Task '{task_description}' removed.")
                return
        print(f"Task '{task_description}' not found.")

    def update_task(self, task_description, new_description, new_date, new_time):
        for task in self.tasks:
            if task.description == task_description:
                task.description = new_description
                task.date = new_date
                task.time = new_time
                print(f"Task '{task_description}' updated.")
                return
        print(f"Task '{task_description}' not found.")

    def show_tasks(self):
        if self.tasks:
            print("Tasks:")
            for i, task in enumerate(self.tasks, 1):
                date_str = task.date.strftime("%Y-%m-%d")
                time_str = task.time.strftime("%H:%M")
                print(f"{i}. {task.description} on {date_str} at {time_str}")
        else:
            print("No tasks.")

    def menu(self):
        print("\nMenu:")
        print("1. Add Task")
        print("2. Remove Task")
        print("3. Update Task")
        print("4. Show Tasks")
        print("5. Exit")

    def run(self):
        while True:
            self.menu()
            choice = input("Enter choice: ")
            if choice == "1":
                description = input("Enter task description: ")
                date_str = input("Enter task date (format: YYYY-MM-DD): ")
                time_str = input("Enter task time (format: HH:MM): ")
                try:
                    date = datetime.strptime(date_str, "%Y-%m-%d")
                    time = datetime.strptime(time_str, "%H:%M")
                    task = Task(description, date, time)
                    self.add_task(task)
                except ValueError:
                    print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
            elif choice == "2":
                description = input("Enter task description to remove: ")
                self.remove_task(description)
            elif choice == "3":
                description = input("Enter task description to update: ")
                new_description = input("Enter new task description: ")
                new_date_str = input("Enter new task date (format: YYYY-MM-DD): ")
                new_time_str = input("Enter new task time (format: HH:MM): ")
                try:
                    new_date = datetime.strptime(new_date_str, "%Y-%m-%d")
                    new_time = datetime.strptime(new_time_str, "%H:%M")
                    self.update_task(description, new_description, new_date, new_time)
                except ValueError:
                    print("Invalid date or time format. Please use YYYY-MM-DD for date and HH:MM for time.")
            elif choice == "4":
                self.show_tasks()
            elif choice == "5":
                print("Exiting...")
                break
            else:
                print("Invalid choice. Please try again.")


if __name__ == "__main__":
    todo_list = TodoList()
    todo_list.run()