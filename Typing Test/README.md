# Key Typing Speed Test - ![Python](https://img.shields.io/badge/Python-3.8%2B-blue)

The **Key Typing Speed Test** is a Python-based GUI application that tests your typing speed and accuracy. It uses the `tkinter` library for the user interface and calculates Words Per Minute (WPM) based on user performance during the typing session.

---

## Features

- Displays a pre-defined set of words from a file (`test_content.txt`) for the user to type.
- Highlights typing accuracy:
  - **Green** background: Correct input.
  - **Red** background: Incorrect input.
- Tracks the number of missed and correctly typed characters.
- Calculates Words Per Minute (WPM) at the end of the test.
- Ends the test after a timer of 60 seconds.

---

## Installation and Setup

### Prerequisites

1. **Python 3.8 or higher** must be installed. You can download Python [here](https://www.python.org/downloads/).
2. A text file named `test_content.txt` must be present in the same directory as the script. It should contain the content you want users to type.

### Required Libraries

No additional installations are necessary as the script only uses Python's built-in libraries (`tkinter` and `time`).

---

## Usage

1. **Prepare the Input File**:
   - Create a file named `test_content.txt` in the same directory as the script.
   - Add the text content for the typing test, ensuring one sentence per line.

2. **Run the Script**:
   Execute the following command:
   ```bash
   python main.py

3. **Start Typing**:
   - A GUI window will display the content to type and an entry field.
   - Type the content shown as quickly and accurately as possible.

4. **Test Results**:
   - Once the content is completed or time runs out, the program will display:- Words Per Minute (WPM).
   - The number of mistakes made.

---

## GUI Layout
1. **Content Display**:
   - Shows the text from `test_content.txt` that users must type.
   - Wraps long content within the window for better readability.

2. **Entry Field**:
   - A text entry field where users type their responses.
   - Changes background color based on typing accuracy:
     - **Green**: Correct.
     - **Red**: Incorrect.

3. **Progress Tracker**:- Displays the typed letters below the entry field to show progress.

4. **Timer**:- Counts down from 60 seconds.

5. **Completion Message**:- Displays the results, including Words Per Minute (WPM) and the number of mistakes.

---

## Code Overview
### Input Handling
Reads content from the file `test_content.txt`, splits it into lines, and creates a list of characters to be typed:
```Python
file = open('test_content.txt')
content = file.read()
content = content.splitlines()
temp_list = []
for word in content:
    for i in range(len(word)):
        temp_list.append(word[i])
```

### Key Press Event
Handles key presses and evaluates user input for accuracy:
```Python
def key_pressed(e):
    ...
    if entered_text.char == char:
        typing_area.configure(background="green")
    else:
        typing_area.configure(background="red")
```

### Timer
Ensures the test ends after 60 seconds and displays the results:
```Python
def timer():
    ...
    completed_message.config(text=f'Your Words Per Minute are: {len(letters) / 5}, you made {len(missed)} mistakes.')
```

### GUI Components
Built using `tkinter`:
- **Labels** for content, progress, timer, and results.
- **Entry Field** for user input.

---

## Example Output
At the end of the test, users see the following results (example):
```bash
Your Words Per Minute are: 40, you made 5 mistakes.
```

---

## Notes
- **Customizable Timer**: Change the `max_time` variable to modify the duration of the test.
- **Word Calculation**: Words are calculated as groups of 5 characters.
- **Input File**: Ensure `test_content.txt` contains sufficient text for the test.



   
