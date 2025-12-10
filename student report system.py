students = []

print("=== Student Report System ===")

while True:
    print("\n1. Add Student")
    print("2. View All Students")
    print("3. Exit")

    choice = input("Choose an option: ")

    if choice == "1":
        name = input("Enter student name: ")
        grade = input("Enter grade: ")
        students.append({"name": name, "grade": grade})
        print("Student added!")

    elif choice == "2":
        print("\n--- Student List ---")
        for s in students:
            print("Name:", s["name"], "| Grade:", s["grade"])

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
