books = []

print("=== LIBRARY BOOK MANAGER ===")

while True:
    print("\n1. Add Book")
    print("2. View Books")
    print("3. Remove Book")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        title = input("Enter book title: ")
        books.append(title)
        print("Book added!")

    elif choice == "2":
        print("\nBooks in Library:")
        for i, b in enumerate(books, 1):
            print(i, "-", b)

    elif choice == "3":
        num = int(input("Enter book number to remove: "))
        if 1 <= num <= len(books):
            books.pop(num - 1)
            print("Book removed!")
        else:
            print("Invalid number!")

    elif choice == "4":
        print("Exiting...")
        break

    else:
        print("Invalid choice!")
