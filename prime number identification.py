num = int(input("Enter a number: "))

print("Even" if num % 2 == 0 else "Odd")

# Prime check
if num > 1:
    for i in range(2, num):
        if num % i == 0:
            print("Not a prime number")
            break
    else:
        print("Prime number")
else:
    print("Not a prime number")
