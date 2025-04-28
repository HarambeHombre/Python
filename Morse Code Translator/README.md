# Morse Code Translator - ![Python](https://img.shields.io/badge/Python-3.10-green)

The **Morse Code Translator** is a Python-based command-line application that allows users to:
- Convert plain text into Morse code.
- Decode Morse code back into plain text.
- Handle errors gracefully by verifying user input.

This project is designed to be user-friendly and highly interactive, offering an intuitive interface for encoding and decoding Morse code.

---

## Features

- **Text to Morse Code Conversion**: Users can encode plain text into Morse code.
- **Morse Code to Text Decoding**: Users can decode valid Morse code back into plain text.
- **Error Handling**: Ensures users provide valid input and displays warnings for invalid choices.
- **Interactive Menu**: A simple menu-driven approach for ease of use.

---

## Requirements

This project requires:
- **Python 3.8 or higher**.
- A file named `classes.py` that contains `encode` and `decode` functions for:
  - Encoding plain text to Morse code.
  - Decoding Morse code back into plain text.

### Libraries
The program does not require additional libraries beyond Python’s built-in modules.

---

## Installation

1. Clone or download this repository to your local machine.
2. Ensure that Python is installed on your system. You can download it from [python.org](https://www.python.org/downloads/).

---

## Usage

1. Run the Program
Navigate to the directory containing the script and execute it:
```bash
python main.py
```

2. Main Menu
The program displays the following menu upon execution:
```
+----------------------+
| Morse code Translate |
| Type:'1' to encode   |
| Type:'2' to decode   |
| Type:'exit' to quit  |
+----------------------+
```

3. Encode Text to Morse Code
- Select option `1` and input the plain text you want to convert to Morse code.
- Example:
```
Selection: 1
Enter text to convert to morse code here: hello
Output: .... . .-.. .-.. ---
```

4. Decode Morse Code to Text
- Select option `2` and input the Morse code you want to decode into plain text.
- Example:
```
Selection: 2
Enter morse code to convert to plain text here: .... . .-.. .-.. ---
Output: hello
```

5. Exit the Program
Type `exit` to quit the program:
Selection:
```
exit
Thank you for using my program! :)
```

---

## Code Overview
### Menu Display and User Interaction
The program uses a loop to keep the menu active until the user decides to exit:
```Python
while active:
    user_choice = input("'1' to encode, '2' to decode, and 'exit' to quit.\nSelection: ").lower()
    ...
```

### Error Handling
Ensures only valid inputs (`1`, `2`, or `exit`) are accepted:
```Python
if user_choice != 'exit' and user_choice != '1' and user_choice != '2':
    print('Invalid selection, please try again.')
```

### Encoding Plain Text to Morse Code
Calls the `encode` function from `classes.py`:
```Python
if user_choice == '1':
    text_to_convert = input('Enter text to convert to morse code here: ').lower()
    encode(text_to_convert)
```

### Decoding Morse Code to Plain Text
Calls the `decode` function from `classes.py`:
```Python
if user_choice == '2':
    fake_input = input('Enter morse code to convert to plain text here: ').lower()
    decode(fake_input)
```

---

## Example Outputs
### Encoding Example
Plain text input:
```
hello world
```

Morse code output:
```
.... . .-.. .-.. ---  .-- --- .-. .-.. -..
```

## Decoding Example
Morse code input:
```
.... . .-.. .-.. ---  .-- --- .-. .-.. -..
```

Plain text output:
```
hello world
```

---

## Notes
- **Morse Code Dictionary**: Ensure the `encode` and `decode` functions use a well-defined dictionary for character-to-Morse code mapping and vice versa.
- **Invalid Inputs**: If an unsupported character or Morse code sequence is entered, the program should handle it gracefully and notify the user.



