import to_do_list
to_do_list.run_list

def run_list():
    to_do_list = []

    while True:
        print("\nMy To-Do List")
        print("1. Add a new task")
        print("2. View all tasks")
        print("3. Remove a task by number")
        print("4. Mark a task as completed")
        print("5. Clear all completed tasks")
        print("6. Quit")

        try:
            choice = int(input("\nChoose an option (1-6): "))
        except ValueError:
            print("Please enter a valid number!")
            continue

        if choice == 1:
            print("Type 'done' when you are finished adding tasks.")
            while True:
                task = input("Enter a new task: ")
                if task.lower() == "done":
                    print("Tasks saved!")
                    break
                elif task.strip() == "":
                    print("Task cannot be empty.")
                else:
                    to_do_list.append(task)
                    print(f"Task '{task}' added.")

        elif choice == 2:
            if not to_do_list:
                print("\nNo tasks in the list yet.")
            else:
                print("\nYour Tasks:")
                for index, task in enumerate(to_do_list, start=1):
                    print(f"{index}. {task}")

        elif choice == 3:
            if not to_do_list:
                print("No tasks to remove!")
            else:
                try:
                    remove = int(input("\nEnter the number of the task to remove: ")) - 1
                    removed_task = to_do_list.pop(remove)
                    print(f"Task '{removed_task}' removed!")
                except (ValueError, IndexError):
                    print("Invalid task number!")

        elif choice == 4:
            if not to_do_list:
                print("No tasks to complete!")
            else:
                try:
                    task_num = int(input("Enter the task number to mark as completed: ")) - 1
                    to_do_list[task_num] = f"{to_do_list[task_num]} - Completed!"
                    print("Task marked as completed!")
                except (ValueError, IndexError):
                    print("Invalid task number!")

        elif choice == 5:
            if not to_do_list:
                print("No tasks to clear!")
            else:
                before = len(to_do_list)
                to_do_list = [task for task in to_do_list if not task.endswith(" - Completed!")]
                removed = before - len(to_do_list)
                print(f"Cleared {removed} completed task(s).")

        elif choice == 6:
            print("Goodbye!")
            break

        else:
            print("Invalid choice, please enter 1-6.")
