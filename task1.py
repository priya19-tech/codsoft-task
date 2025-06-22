import json
import os

FILENAME = "tasks.json"

# Load tasks from JSON file
def load_tasks():
    if os.path.exists(FILENAME):
        with open(FILENAME, 'r') as file:
            return json.load(file)
    return []

# Save tasks to JSON file
def save_tasks(tasks):
    with open(FILENAME, 'w') as file:
        json.dump(tasks, file, indent=4)

# Display task list
def display_tasks(tasks):
    if not tasks:
        print(" No tasks available.")
        return
    print("\n Your To-Do List:")
    for idx, task in enumerate(tasks, start=1):
        status = "✔️" if task['done'] else "❌"
        print(f"{idx}. {task['task']} [{status}]")

# Add a new task
def add_task(tasks):
    task = input("Enter new task: ")
    tasks.append({'task': task, 'done': False})
    print("Task added!")

# Mark a task as done
def mark_done(tasks):
    display_tasks(tasks)
    try:
        num = int(input("Enter task number to mark as done: ")) - 1
        if 0 <= num < len(tasks):
            tasks[num]['done'] = True
            print("Task marked as done.")
        else:
            print(" Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

# Delete a task
def delete_task(tasks):
    display_tasks(tasks)
    try:
        num = int(input("Enter task number to delete: ")) - 1
        if 0 <= num < len(tasks):
            removed = tasks.pop(num)
            print(f" Task '{removed['task']}' deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print(" Please enter a valid number.")

# Main menu loop
def main():
    tasks = load_tasks()
    while True:
        print("\n To-Do Menu:")
        print("1. View Tasks")
        print("2. Add Task")
        print("3. Mark Task as Done")
        print("4. Delete Task")
        print("5. Exit")

        choice = input("Choose an option (1-5): ")

        if choice == '1':
            display_tasks(tasks)
        elif choice == '2':
            add_task(tasks)
        elif choice == '3':
            mark_done(tasks)
        elif choice == '4':
            delete_task(tasks)
        elif choice == '5':
            save_tasks(tasks)
            print(" Exiting... Tasks saved.")
            break
        else:
            print(" Invalid option. Try again.")

if __name__ == "__main__":
    main()
