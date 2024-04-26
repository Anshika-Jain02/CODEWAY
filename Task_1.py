''' A To-Do List application is a useful project that helps users manage
 and organize their tasks efficiently. This project aims to create a
 command-line or GUI-based application using Python, allowing users
 to create, update, and track their to-do lists.
 '''

class TodoList:
    def __init__(self):
        self.tasks = []

    def add_task(self, task):
        self.tasks.append(task)

    def list_tasks(self):
        for i, task in enumerate(self.tasks, 1):
            print(f"{i}. {task}")

    def complete_task(self, task_index):
        del self.tasks[task_index - 1]

    def save_tasks(self, filename):
        with open(filename, 'w') as f:
            for task in self.tasks:
                f.write(task + '\n')

    def load_tasks(self, filename):
        with open(filename, 'r') as f:
            self.tasks = [line.strip() for line in f]

def main():
    todo_list = TodoList()

    # Load tasks from a file if it exists
    try:
        todo_list.load_tasks("tasks.txt")
    except FileNotFoundError:
        pass

    while True:
        print("\n1. Add Task")
        print("2. List Tasks")
        print("3. Complete Task")
        print("4. Save Tasks")
        print("5. Quit")

        choice = input("Enter your choice: ")

        if choice == "1":
            task = input("Enter task: ")
            todo_list.add_task(task)
        elif choice == "2":
            todo_list.list_tasks()
        elif choice == "3":
            task_index = int(input("Enter task index to complete: "))
            todo_list.complete_task(task_index)
        elif choice == "4":
            todo_list.save_tasks("tasks.txt")
            print("Tasks saved successfully.")
        elif choice == "5":
            break
        else:
            print("Invalid choice. Please try again.")

if __name__ == "__main__":
    main()
