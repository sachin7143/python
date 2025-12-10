name = input("Enter student name: ")
roll = input("Roll number: ")

marks = []
print("Enter marks of 5 subjects:")

for i in range(5):
    m = float(input(f"Subject {i+1}: "))
    marks.append(m)

total = sum(marks)
percent = total / 5

print("\n=== MARKSHEET ===")
print("Name:", name)
print("Roll No:", roll)
print("Total:", total)
print("Percentage:", percent)

if percent >= 90:
    print("Grade: A")
elif percent >= 75:
    print("Grade: B")
elif percent >= 60:
    print("Grade: C")
else:
    print("Grade: D")
