import json

print("Project number 1 - Text to morse code converter")

user_text = input("Please insert text you want to convert: ")
lift_of_letters = list(user_text)

with open('morse-alphabet.json', "r") as file:
    alphabet = json.load(file)
    for letter in lift_of_letters:
        print(alphabet[letter])

