# Tic-Tac-Toe Python Game - ![Python](https://img.shields.io/badge/Python-3.10-green)

**Tic-Tac-Toe Python Game** is a console-based implementation of the classic game designed for two players, where each player alternates turns to place their marker ("X" or "O") on a 3x3 grid. The game dynamically updates the board and checks for wins, ties, or invalid moves.

---

## Features

- Two-player mode: Alternates turns for players "X" and "O".
- Dynamic board rendering: The game board updates after every move.
- Win detection: Checks all possible winning combinations.
- Tie detection: Ends the game in a tie if all spaces are filled and there is no winner.
- Input validation: Ensures proper marker and grid space selection.

---

## Requirements

No external libraries are required. The game runs using Python's built-in capabilities.

### Prerequisites
- Python 3.8 or higher.

---

## Installation

1. Clone this repository or copy the script file.
2. Ensure Python is installed on your system. You can download Python [here](https://www.python.org/downloads/).

---

## Usage

1. Open a terminal or command prompt.
2. Navigate to the directory containing the script.
3. Run the script:
   ```bash
   python main.py
   ```

---

## Gameplay Instructions
1. The initial board is displayed in the terminal:Tic-Tac-Toe
```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```
2. Players alternate turns to select their marker ("X" or "O") and choose a grid space using its number.
3. After each turn:
   - The board updates dynamically.
   - Input validation ensures that players cannot overwrite existing markers or select invalid spaces.
4. The game checks for a win or tie after every move.
5. If a player wins or the game ends in a tie, a message is displayed, and the game exits.

---

## Code Breakdown
### Initial Setup
The game begins with a predefined dictionary for the grid spaces and initializes variables:
```Python
values_dict = {1: 1, 2: 2, 3: 3, 4: 4, 5: 5, 6: 6, 7: 7, 8: 8, 9: 9}
tie_check = values_dict.copy()
game_on = True
```

### Board Display
Displays the board dynamically after every move:
```Python
playing_area = f'''
Tic-Tac-Toe
 {values_dict[1]} | {values_dict[2]} | {values_dict[3]}
---+---+---
 {values_dict[4]} | {values_dict[5]} | {values_dict[6]}
---+---+---
 {values_dict[7]} | {values_dict[8]} | {values_dict[9]}
'''
```

### Player Input and Validation
Players select their marker ("X" or "O") and grid space. The script ensures valid entries:
```Python
user_selection = input('Type either "X" or "O" to select who\'s turn it is: ').upper()
if user_selection != 'X' and user_selection != 'O':
    print('Not valid, please try again.')
grid_location = input(f'Input a number to add an "{user_selection}" to that space: ')
if int(grid_location) in values_dict:
    ...
```

### Win and Tie Logic
Checks all possible winning combinations and conditions for a tie:
```Python
if values_dict[1] == 'X' and values_dict[2] == 'X' and values_dict[3] == 'X':
    print('"X" wins!')
    game_on = False
if not tie_check:
    print('Tie Game!')
    game_on = False
```

### Example Output
Here’s an example of gameplay:
1. Initial Board:Tic-Tac-Toe
```
 1 | 2 | 3
---+---+---
 4 | 5 | 6
---+---+---
 7 | 8 | 9
```

2. Player X's Turn:
```
Type either "X" or "O" to select who's turn it is: X
Input a number to add an "X" to that space: 5
Tic-Tac-Toe
 1 | 2 | 3
---+---+---
 4 | X | 6
---+---+---
 7 | 8 | 9
```

3. Final Message:
```
"X" wins!
```

---

## Notes
- **Scalability**: This implementation is limited to a 3x3 grid. Expanding to larger boards would require modifying the win logic.
- **Replayability**: To restart the game, rerun the script.
- **Customization**: Add features like AI opponents or user-defined grid sizes.



   
