tasks = []

print("=== To-Do List ===")

while True:
    print("\n1. Add Task")
    print("2. View Tasks")
    print("3. Remove Task")
    print("4. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        task = input("Enter task: ")
        tasks.append(task)
        print("Task added!")
    
    elif choice == "2":
        print("\nYour Tasks:")
        for i, t in enumerate(tasks, start=1):
            print(i, "-", t)

    elif choice == "3":
        num = int(input("Task number to remove: "))
        if 1 <= num <= len(tasks):
            tasks.pop(num - 1)
            print("Task removed!")
        else:
            print("Invalid number!")
    
    elif choice == "4":
        print("Exiting program.")
        break

    else:
        print("Invalid option!")
