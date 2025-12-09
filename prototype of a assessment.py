questions = [
    ("2 + 2 = ?", "4"),
    ("Capital of India?", "delhi"),
    ("Color of banana?", "yellow"),
    ("5 x 5 = ?", "25"),
    ("Ocean on Earth?", "pacific")
]

score = 0

print("=== QUIZ ===")

for q, ans in questions:
    print("\n" + q)
    user = input("Answer: ").lower()
    if user == ans:
        print("Correct!")
        score += 1
    else:
        print("Wrong!")

percent = (score / len(questions)) * 100
print("\nYour Score:", score)
print("Percentage:", percent, "%")
