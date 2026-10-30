
# Day 6 - Adventure Island

## 100 Days of Python Challenge

### Project: Adventure Island - Text-Based Adventure Game

For Day 6 of my 100 Days of Python Challenge, I built an interactive text-based adventure game called Adventure Island.

This was my most involved Python project so far.

The game combines functions, conditional statements, loops, user input, return values, imported modules, and terminal colors.

I also experimented with separating my program into multiple Python files to make the code easier to organize and maintain.

## Project Description

Adventure Island is a text-based adventure where the player must make decisions to survive and find hidden treasure.

The player explores a mysterious island, encounters dangerous situations, and must choose the correct path to reach the treasure.

Each decision affects whether the player survives or the game ends.

## Gameplay

### Stage 1 - The Crossroads

The player arrives at a crossroads and must choose between two paths.

- Lake: The player safely reaches a mysterious lake.
- Mountain: The player falls off a cliff. Game Over!

### Stage 2 - The Lake

After reaching the lake, the player discovers an old boat sitting on the shore.

The player must decide how to cross.

- Swim: A deadly lake creature attacks. Game Over!
- Boat: The player safely crosses the lake.

### Stage 3 - The Temple

After crossing the lake, the player discovers a mysterious stone temple containing three doors.

- Red Door: The player is engulfed in flames. Game Over!
- Blue Door: The player encounters deadly beasts. Game Over!
- Yellow Door: The player discovers the hidden treasure and wins!

## Project Structure

```text
Day 6 - Adventure Island/
│
├── main.py
├── functions.py
└── README.md
```

### main.py

This file controls the overall flow of the game.

It imports the functions from `functions.py` and calls them in the correct order.

Nested conditional statements ensure the player can only continue after surviving the previous challenge.

### functions.py

This file contains the functions responsible for storytelling, player choices, and survival outcomes.

The functions include:

- `game_intro()`
- `story_element1()`
- `crossroads()`
- `story_element2()`
- `lake_crossing()`
- `story_element3()`
- `treasure_room()`

## Python Concepts Learned

### 1. Functions

I practiced creating multiple functions to organize different sections of the game.

Each function handles a specific task, making the program easier to understand.

### 2. Importing Custom Modules

I learned how to separate Python code into multiple files and import my own functions.

```python
import functions as game
```

This allows me to call functions using the `game` alias.

```python
game.game_intro()
```

### 3. Return Values

I learned how functions can return values to communicate information to other parts of a program.

For example:

```python
return True
```

indicates that the player survived.

```python
return False
```

indicates that the player lost.

### 4. Nested Conditional Statements

I used nested `if` statements to control the flow of the game.

```python
if game.crossroads():
    game.story_element2()

    if game.lake_crossing():
        game.story_element3()

        if game.treasure_room():
            print("Congratulations! You completed Adventure Island!")
```

This ensures the player cannot continue after a Game Over.

### 5. While Loops and Input Validation

I used `while True` loops to repeatedly ask players for input until they enter a valid option.

I also used:

```python
.strip().lower()
```

to remove extra spaces and make input case-insensitive.

### 6. The Time Module

I experimented with the built-in `time` module to create suspense between story messages.

```python
import time

time.sleep(2)
```

This pauses the program for two seconds before continuing.

### 7. Terminal Colors

I learned how to use ANSI escape codes to display colored messages in the terminal.

```python
RED = "\033[31m"
GREEN = "\033[32m"
YELLOW = "\033[33m"
CYAN = "\033[36m"
RESET = "\033[0m"
```

I used different colors for successful decisions, dangerous situations, and winning the game.

I also learned the importance of resetting terminal colors after displaying colored text.

## Challenges Encountered


### Understanding Break vs Return

I learned that `break` exits a loop, while `return` exits a function and can send information back to the calling code.

This became especially important when controlling whether the player survived.

### Connecting Functions

One challenge was preventing the game from continuing after the player died.

I solved this using Boolean return values and nested conditional statements.

### Terminal Colors

I experimented with ANSI escape codes to make the game more visually interesting.

I discovered that terminal colors need to be reset to prevent subsequent messages from inheriting the previous color.

## How to Run

1. Make sure Python is installed.
2. Open the Day 6 project folder in VS Code.
3. Open the integrated terminal.
4. Run:

```bash
python main.py
```

Follow the instructions displayed in the terminal and make your decisions.

## Winning Path

To successfully complete Adventure Island, choose:

```text
Lake
Boat
Yellow
```

These choices allow the player to survive the adventure and discover the treasure.

## What I Learned

- How to organize a larger Python program using functions
- How to create and import custom modules
- How to use Boolean return values
- How to control program flow with nested conditionals
- How to validate user input
- How to use loops for repeated questions
- How to add delays with the time module
- How to add terminal colors using ANSI escape codes
- How to debug logical errors in a multi-stage program

## Reflection

Day 6 was a major step forward in my Python learning journey.

I started with a simple adventure introduction and gradually expanded it into a complete interactive game.

One of my biggest accomplishments was independently experimenting with separating my code into multiple files and importing my own functions.

I also gained a much stronger understanding of how `return True` and `return False` can control the flow of a program.

This project helped me see how individual programming concepts work together to create something larger.

## Future Improvements

Some features I would like to explore in future versions include:

- Adding more story paths
- Introducing a player health system
- Creating an inventory system
- Adding randomized encounters
- Allowing players to restart after Game Over
- Expanding the island with additional locations

---

**Day 6 Complete - 100 Days of Python Challenge**
