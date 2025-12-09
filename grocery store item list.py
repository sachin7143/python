shopping = []

while True:
    print("\n1. Add Item")
    print("2. View List")
    print("3. Remove Item")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        item = input("Item name: ")
        shopping.append(item)
        print("Added!")

    elif choice == "2":
        print("\nYour Shopping List:")
        for i, item in enumerate(shopping, 1):
            print(i, "-", item)

    elif choice == "3":
        num = int(input("Item number to remove: "))
        if 1 <= num <= len(shopping):
            shopping.pop(num - 1)
            print("Removed!")
        else:
            print("Invalid number!")

    elif choice == "4":
        print("Exiting.")
        break

    else:
        print("Invalid choice!")
