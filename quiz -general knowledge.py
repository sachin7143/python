questions = [
    ("What is the capital of France?", "paris"),
    ("5 + 7 = ?", "12"),
    ("What color is the sky?", "blue")
]

score = 0

print("=== Quiz Game ===")

for q, ans in questions:
    print("\nQuestion:", q)
    user = input("Your answer: ").lower()

    if user == ans:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

print("\nYour final score:", score, "/", len(questions))
