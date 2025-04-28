# Block Breaker Game ![Python](https://img.shields.io/badge/Python-3.x-blue)

**Block Breaker Game** is a fun and interactive arcade-style game built using `pygame`. The objective is to break all the bricks using a bouncing ball while avoiding losing all your lives. With increasing difficulty as the game progresses, this project provides an exciting challenge for players of all ages!

---

## Features

- **Dynamic Gameplay**:
  - Paddle movement controlled by the mouse.
  - Ball physics with collision detection for bricks, paddle, and screen boundaries.
- **Challenging Levels**:
  - Gradual difficulty increase as the brick count reduces.
  - Color changes for bricks, paddle, and ball at key milestones.
- **Score Tracking**:
  - Gain points by breaking bricks.
- **Lives System**:
  - Lose lives if the ball falls below the paddle.
- **Win and Game Over States**:
  - Displays "Game Over" when all lives are lost.
  - Displays "You Won!" upon clearing all the bricks.

---

## Requirements

### Python Libraries
The following Python libraries are required:
- `pygame`: A library for creating graphical and interactive games.

---

System Requirements
- Python 3.8 or higher.
- A system capable of running `pygame` (Windows, macOS, or Linux).


Installation
1. Clone this repository or download the code file:
```bash
git clone https://github.com/HarambeHombre/Python.git
```
2. Navigate to the project directory:
```bash
cd block-breaker
```
3. Install the required library:
```bash
pip install pygame
```
4. Run the game:
```bash
python main.py
```

---

## Controls
- **Paddle Movement**: Use the mouse to control the paddle's horizontal position.
- **Restart Game**: Press the **Spacebar** when the game is over or won.

---

## Gameplay
### Objective
Break all the bricks using the ball while preventing the ball from falling below the paddle.
### Scoring
- Earn 10 points for each brick you break.
- The total score is displayed in the top left of the screen.

### Lives
- You start with 3 lives.
- Lose a life if the ball falls below the paddle.
- Game over when all lives are lost.

### Winning
- Clear all bricks to win the game.
- Press **Spacebar** to restart after winning.

---

## Game Logic
### Paddle and Ball Interaction
- The paddle reflects the ball upward upon contact.
- The paddle's width reduces and colors change as bricks are cleared, increasing difficulty.

### Brick Collision
- Each collision with a brick removes the brick and increases the score.
- The ball's direction reverses upon collision.

### Difficulty Progression
- **Less than 30 bricks**: Paddle width reduces to 100 pixels, colors shift to orange/red.
- **Less than 15 bricks**: Paddle width reduces to 75 pixels, colors change randomly for added challenge.

---

## Example Output
### Initial State
- Paddle width: 200 pixels.
- Bricks arranged in rows.
- Ball starts at the center of the screen.

### After Clearing Some Bricks
- Paddle width reduces to 100 pixels.
- Bricks and ball colors change to indicate increasing difficulty.

### Winning State
Displays:
```
You Won! Press Space to start a new game.
```

### Game Over State
Displays:
```
Game Over! Press Space to start a new game.
```

---

## Notes
- **Physics Handling**: The ball direction reverses upon collision with walls, paddle, or bricks.
- **Dynamic Difficulty**: The paddle's width and colors dynamically adjust to increase challenge as bricks are cleared.
- **Replayability**: Players can restart the game after winning or losing by pressing the Spacebar.



