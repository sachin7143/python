contacts = {}

print("=== Contact Book ===")

while True:
    print("\n1. Add Contact")
    print("2. View Contacts")
    print("3. Search Contact")
    print("4. Exit")

    choice = input("Choose option: ")

    if choice == "1":
        name = input("Name: ")
        phone = input("Phone: ")
        contacts[name] = phone
        print("Contact saved!")

    elif choice == "2":
        print("\n--- Contact List ---")
        for name, phone in contacts.items():
            print(name, ":", phone)

    elif choice == "3":
        search = input("Enter name to search: ")
        if search in contacts:
            print(search, ":", contacts[search])
        else:
            print("Not found!")

    elif choice == "4":
        print("Exiting contact book.")
        break

    else:
        print("Invalid option!")
