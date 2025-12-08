text = input("Enter a sentence: ")

words = text.split()
print("Total words:", len(words))
print("Words:")

for w in words:
    print("-", w)
