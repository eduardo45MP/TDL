import os

# File name to store tasks
TODO_FILE = "tasks.txt"

def load_tasks():
    tasks = []
    if os.path.exists(TODO_FILE):
        with open(TODO_FILE, "r") as file:
            tasks = file.read().splitlines()
    return tasks

def save_tasks(tasks):
    with open(TODO_FILE, "w") as file:
        file.write("\n".join(tasks))

def list_tasks(tasks):
    if not tasks:
        print("No tasks in the list.")
    else:
        print("Pending tasks:")
        for i, task in enumerate(tasks, 1):
            print(f"{i}. {task}")

def add_task(tasks, task_description):
    tasks.append(task_description)
    save_tasks(tasks)
    print(f"Task '{task_description}' added successfully!")

def complete_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        completed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task '{completed_task}' marked as completed!")
    else:
        print("Invalid task index.")

def remove_task(tasks, task_index):
    if 1 <= task_index <= len(tasks):
        removed_task = tasks.pop(task_index - 1)
        save_tasks(tasks)
        print(f"Task '{removed_task}' removed successfully!")
    else:
        print("Invalid task index.")

def main():
    tasks = load_tasks()

    while True:
        print("\nOptions:")
        print("1. List tasks")
        print("2. Add task")
        print("3. Mark task as completed")
        print("4. Remove task")
        print("5. Exit")

        choice = input("Choose an option: ")

        if choice == "1":
            list_tasks(tasks)
        elif choice == "2":
            task_description = input("Enter task description: ")
            add_task(tasks, task_description)
        elif choice == "3":
            list_tasks(tasks)
            task_index = int(input("Enter the task number to mark as completed: "))
            complete_task(tasks, task_index)
        elif choice == "4":
            list_tasks(tasks)
            task_index = int(input("Enter the task number to remove: "))
            remove_task(tasks, task_index)
        elif choice == "5":
            print("Exiting the application.")
            break
        else:
            print("Invalid option. Please try again.")

if __name__ == "__main__":
    main()

