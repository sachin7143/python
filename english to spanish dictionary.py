dictionary = {
    "hello": "hola",
    "cat": "gato",
    "dog": "perro",
    "food": "comida"
}

word = input("Enter an English word: ")

if word in dictionary:
    print("Spanish:", dictionary[word])
else:
    print("Word not found!")
