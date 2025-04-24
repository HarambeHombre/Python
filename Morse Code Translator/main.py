#Morse code translator
#Create a program that converts plain text to morse code.
#EXTRA: Make a decoder to convert morse code back into plain text.
#ADDED: Error checking, incase an invalid response is given.
#TODO 1. Create dictionary for alphabet, and morse code
from classes import encode, decode

print('''
+----------------------+
| Morse code Translate |
| Type:'1' to encode   |
| Type:'2' to decode   |
| Type:'exit' to quit  |
+----------------------+
''')
user_choice = ''
active = True
while active:

    user_choice = text_to_convert = input("'1' to encode, '2' to decode, and 'exit' to quit.\nSelection: ").lower()
    if user_choice != 'exit' and user_choice != '1' and user_choice != '2':
        print('Invalid selection, please try again.')

    if user_choice == 'exit':
        print('Thank you for using my program! :)')
        active = False

    if user_choice == '1':
        text_to_convert = input('Enter text to convert to morse code here: ').lower()
        encode(text_to_convert)

    if user_choice == '2':
        fake_input = input('Enter morse code to convert to plain text here: ').lower()
        decode(fake_input)
