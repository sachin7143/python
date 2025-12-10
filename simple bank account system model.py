balance = 0

print("=== Bank Account ===")

while True:
    print("\n1. Deposit")
    print("2. Withdraw")
    print("3. Check Balance")
    print("4. Exit")

    choice = input("Choose: ")

    if choice == "1":
        amt = float(input("Enter amount: "))
        balance += amt
        print("Deposited!")

    elif choice == "2":
        amt = float(input("Enter amount: "))
        if amt <= balance:
            balance -= amt
            print("Withdrawn!")
        else:
            print("Insufficient balance!")

    elif choice == "3":
        print("Balance:", balance)

    elif choice == "4":
        print("Goodbye!")
        break

    else:
        print("Invalid option!")
