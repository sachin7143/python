secret = "python"
display = ["_"] * len(secret)

print("=== GUESS THE WORD ===")

while "_" in display:
    print("\nWord:", " ".join(display))
    letter = input("Enter a letter: ").lower()

    if letter in secret:
        for i in range(len(secret)):
            if secret[i] == letter:
                display[i] = letter
        print("Correct!")
    else:
        print("Wrong letter!")

print("\nYou guessed the word:", secret)
