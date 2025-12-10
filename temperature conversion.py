print("=== Temperature Converter ===")
print("1. C to F")
print("2. F to C")

choice = input("Choose: ")

if choice == "1":
    c = float(input("Enter Celsius: "))
    f = (c * 9/5) + 32
    print("Fahrenheit:", f)

elif choice == "2":
    f = float(input("Enter Fahrenheit: "))
    c = (f - 32) * 5/9
    print("Celsius:", c)
else:
    print("Invalid choice!")
