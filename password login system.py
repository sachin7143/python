username = "admin"
password = "1234"

print("=== Login System ===")

for attempt in range(3):
    user = input("Username: ")
    pwd = input("Password: ")

    if user == username and pwd == password:
        print("Login successful!")
        break
    else:
        print("Wrong credentials. Try again.")

if user != username or pwd != password:
    print("Too many failed attempts.")
