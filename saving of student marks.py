marks = []

print("Enter 5 subject marks:")
for i in range(5):
    m = float(input("Subject " + str(i+1) + ": "))
    marks.append(m)

avg = sum(marks) / 5

print("\nAverage:", avg)

if avg >= 90:
    print("Grade: A")
elif avg >= 75:
    print("Grade: B")
elif avg >= 60:
    print("Grade: C")
else:
    print("Grade: D")
