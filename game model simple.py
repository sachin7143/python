import random

secret = random.randint(1, 50)

while True:
    guess = int(input("Guess a number 1–50: "))
    if guess < secret:
        print("Too low!")
    elif guess > secret:
        print("Too high!")
    else:
        print("Correct!")
        break
