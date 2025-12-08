print("=== CURRENCY CONVERTER ===")
print("1. USD to INR")
print("2. INR to USD")

choice = input("Choose: ")

if choice == "1":
    usd = float(input("Enter USD: "))
    print("INR:", usd * 83.2)

elif choice == "2":
    inr = float(input("Enter INR: "))
    print("USD:", inr / 83.2)

else:
    print("Invalid option!")
