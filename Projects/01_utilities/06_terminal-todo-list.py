# Terminal Based Task List Manager 
import os
TASK_FILE = "task.txt"

def load_task():
    task = []
    if(os.path.exists(TASK_FILE)):
        with open(TASK_FILE, "r", encoding="utf-8") as f:
            for line in f:
                # rsplit(separator, how many spillting?): right side spilt, will read the string from the RHS
                text, status = line.strip().rsplit("||", 1)
                task.append({"text": text, "status": status == "done"})
    return task

def save_task(task):
    with open(TASK_FILE, "w", encoding="utf-8") as f:
        for task in task:
            status = "done" if task["status"] else "not_done"
            f.write(f"{task['text']} || {status}\n")

def display_task(task):
    if not task:
        print(f"No tasks found.")
    else:
        for i, task in enumerate(task, 1):
            checkbox = '✅' if task['status'] else " "
            print(f"{i}. [{checkbox}] {task['text']}")
    print()

def task_manager():
    tasks = load_task()

    while True:
        print("\n----------Task List Manager----------")
        print("1. Add task")
        print("2. View task")
        print("3. Mark task as complete")
        print("4. Delete task")
        print("5. Exit")

        choice = int(input("Choose an option: "))
        match choice:
            case 1:
                text = input("Enter your task: ")
                if text:
                    tasks.append({"text": text, "status": False})
                else:
                    print("Task cannot be added.")

            case 2:
                display_task(tasks)

            case 3:
                display_task(tasks)
                try:
                    num = int(input("Enter task number to be completed: "))
                    if 1 <= num <= len(tasks):
                        tasks[num - 1]["status"] = True
                        save_task(tasks)
                        print("Task marked as done.")
                    else:
                        print("Invalid Number found.")
                except ValueError:
                    print("Please enter a valid number.")

            case 4:
                display_task(tasks)
                try:
                    num = int(input("Enter task number to be completed: "))
                    if 1 <= num <= len(tasks):
                        removed = tasks.pop(num - 1)
                        save_task(tasks)
                        print(f"Task removed: {removed['text']}")
                    else:
                        print("Invalid Number found.")
                except ValueError:
                    print("Please enter a valid number.")

            case 5:
                print("Existing task manger.")
                break

            case _:
                print("Please Choose a valid option.")

task_manager()