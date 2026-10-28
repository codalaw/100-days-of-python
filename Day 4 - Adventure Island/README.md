# Day 4 - Nested Conditions and Loops

## 100 Days of Python Challenge

### Project: Enchanted Forest Adventure

## Overview

On Day 4 of my 100 Days of Python Challenge, I built an interactive text-based adventure game called **Enchanted Forest**.

The player decides whether to enter a mysterious forest and, if they enter, chooses between different paths that lead to different outcomes.

This project helped me understand how to combine conditional statements with nested loops to control the flow of a program.

## What I Learned

- Writing nested `if`, `elif`, and `else` statements
- Using `while True` loops to repeat questions
- Nesting loops inside conditional statements
- Using `break` to exit loops
- Using `continue` to restart a loop
- Handling invalid user inputs
- Using `.strip()` and `.lower()` to normalize user input
- Understanding Python indentation and program flow
- Debugging logic errors

## How the Game Works

1. The player is welcomed to the Enchanted Forest.
2. The player chooses whether to enter the forest.
3. If they decline, the adventure ends.
4. If they enter, they reach a fork in the road.
5. The player chooses between three options:
   - **River:** Discover a peaceful waterfall.
   - **Mountain:** Encounter a sleeping dragon.
   - **Leave:** Exit the enchanted forest.
6. Invalid choices cause the question to repeat.
7. The game ends after the player makes a valid path choice.

## How to Run

Make sure Python is installed.

Open a terminal inside the project folder and run:

```bash
python forest_path.py
```

Follow the on-screen prompts to play the game.

## Challenges I Faced

One of the biggest challenges was understanding how nested loops and conditional statements work together.

I encountered several issues involving indentation, misplaced `else` statements, and loops that continued running after the adventure was supposed to end.

Through debugging, I learned that `break` only exits the loop it belongs to and that indentation determines how Python groups instructions.

## Reflection

Today I learned that writing a working program involves more than knowing Python syntax.

Understanding the order in which code executes is just as important.

By debugging my Enchanted Forest game, I gained more confidence using nested conditions and loops to create interactive programs.

## Next Up

**Day 5 - Treasure Island Adventure**

Build a larger interactive adventure game with multiple decisions, branching paths, and winning or losing outcomes.