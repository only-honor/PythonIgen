def main():
    tasks = []
    while True:
        print("\nTask Manager")
        print("1. Add Task")
        print("2. View Tasks")
        print("3. Remove Task")
        print("4. Exit")
        choice = int(input("Enter your choice: "))
        if choice == 1:
            add_task(tasks)
        elif choice == 2:
            view_tasks(tasks)
        elif choice == 3:
            remove_task(tasks)
        elif choice == 4:
            print("Exiting...")
            break
        else:
            print("Invalid choice")


def add_task(tasks):
    task = input("Enter a task: ")
    tasks.append(task)
    print(f"Task", task, "added successfully.")


def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        print("Tasks:")
        i = 0
        while i < len(tasks):
            print(tasks[i])
            i+=1

def remove_task(tasks):
    if not tasks:
        print("No tasks found.")
    else:
        task = int(input("Enter the task number to remove (numbers start from 0): "))
        if task < 0 or task >= len(tasks):
            print("Invalid task number.")
        else:
            removed_task = tasks.pop(task)
            print("Task", removed_task, "removed successfully.")
        

if  __name__ == "__main__":
    main()