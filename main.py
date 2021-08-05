import json

START = True

print("Welcome to my first Python project - Morse Code Converter")

while START:
    response = input(
        "What do you want to do? If you wish to convert text to morse enter '1'. If you wish to convert morse to text type '2' and for exitting the program type '3': ")
    if response == '1':
        user_text = input("Please insert text you want to convert: ")
        list_of_letters = list(user_text)
        converted_word = []
        with open('morse-alphabet.json', "r") as file:
            alphabet = json.load(file)
            for letter in list_of_letters:
                letter = letter.lower()
                if letter == " ":
                    converted_word.append(" ")
                else:
                    converted_word.append(alphabet[letter])
            print(' '.join(converted_word))
    elif response == '2':
        user_morse = input("Please insert morse code you want to convert: ")
        list_of_chars = user_morse.split()
        converted_word = []
        for char in list_of_chars:
            with open('morse-alphabet.json', "r") as file:
                alphabet = json.load(file)
                for key, value in alphabet.items():
                    if char == value:
                        converted_word.append(key)
                        break
                    elif char == "/":
                        converted_word.append(' ')
                        break
        print(''.join(converted_word))
    elif response == '3':
        START = False
    else:
        print("Wrong innput.")


