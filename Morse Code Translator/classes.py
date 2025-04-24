from dictionary import morse_dict, morse_decode
import time

def encode(message):
    i = 0
    converted_text = ''
    for char in message:
        if char[i] in morse_dict:
            converted_text += f'{morse_dict[char[i]]}   '
        elif char[i] == ' ':
            converted_text += f'       '
        elif char not in morse_dict:
            print(f"Invalid Response '{char}', please try again.")
            time.sleep(1)
    print(converted_text)

def decode(message2):
    i = 0
    message = []
    new_message = ''
    word = message2.split('          ')
    for char in word:
        letter = char.split('   ')
        message.append(letter)
    for line in message:
        for item in line:
            if item in morse_decode:
                new_message += morse_decode[item]
            else:
                print(f"Invalid Response '{item}', please try again.")
                time.sleep(1)
        new_message += ' '
    print(new_message)
