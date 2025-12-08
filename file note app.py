print("=== FILE NOTE APP ===")

while True:
    print("\n1. Write Note")
    print("2. Read Notes")
    print("3. Exit")

    choice = input("Choose: ")

    if choice == "1":
        text = input("Enter note: ")
        f = open("notes.txt", "a")
        f.write(text + "\n")
        f.close()
        print("Saved!")

    elif choice == "2":
        print("\nYour Notes:")
        f = open("notes.txt", "r")
        print(f.read())
        f.close()

    elif choice == "3":
        print("Goodbye!")
        break

    else:
        print("Invalid choice!")
