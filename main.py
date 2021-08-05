import json

print("Project number 1 - Text to morse code converter")

user_text = input("Please insert text you want to convert: ")

with open('morse-alphabet.json', "r") as file:
    alphabet = json.load(file)
    print(alphabet['a'])

