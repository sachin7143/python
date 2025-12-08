attendance = {}

print("=== ATTENDANCE SYSTEM ===")

while True:
    print("\n1. Mark Present")
    print("2. View Attendance")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        name = input("Enter student name: ")
        attendance[name] = "Present"
        print("Attendance marked!")

    elif choice == "2":
        print("\n--- Attendance List ---")
        for student, status in attendance.items():
            print(student, ":", status)

    elif choice == "3":
        print("Exiting...")
        break

    else:
        print("Invalid option!")
