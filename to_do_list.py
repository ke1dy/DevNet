to_do_list = []
  
while True:

    print("\nMy To Do List")
    print("1. Add a new task")
    print("2. View all tasks")
    print("3. Remove a task by their number")
    print("4. Mark a task as completed")

    choice = int(input("\nChoose an option above: "))
    if choice == 1:
        print("Type 'done' to stop")
        while True:
            task = input("Enter a new task: ")
            if task == "done":
                print("Saving to your list")
                break
            else:
                to_do_list.append(task)
                continue
                
    elif choice == 2:
        for index, tasks in enumerate(to_do_list, start = 1):
            print(f"Task {index}: {tasks}")
    
    elif choice == 3:
        remove = int(input("\nRemove a task: "))
        remove = remove - 1
        to_do_list.remove(to_do_list[remove]) 
    
    elif choice == 4:
        removeNum = int(input("Choose a task that you have completed: "))
        removeNum -= 1
        to_do_list[removeNum] = f"{to_do_list[removeNum]} - Completed!"