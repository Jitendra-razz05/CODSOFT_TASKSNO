tasks = []

while True:
    print("\n===== TO-DO LIST =====")
    print("1. Add Task")
    print("2. View Tasks")
    print("3. Update Task")
    print("4. Delete Task")
    print("5. Mark Completed")
    print("6. Exit")


    choice = input("Enter your choice: ")


    if choice == "1":
        task = input("Enter task: ")
        tasks.append({"name": task, "done": False})
        print("Task added successfully!")
        

    elif choice == "2":
        for i, task in enumerate(tasks, 1):
            status = "Completed" if task["done"] else "Pending"
            print(i, task["name"], "-", status)


    elif choice == "3":
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["name"] = input("Enter new task: ")
            print("Task updated!")


    elif choice == "4":
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num-1)
            print("Task deleted!")


    elif choice == "5":
        num = int(input("Enter task number: "))
        if 1 <= num <= len(tasks):
            tasks[num-1]["done"] = True
            print("Task completed!")


    elif choice == "6":
        print("Thank you!")
        break
    

    else:
        print("Invalid choice!")