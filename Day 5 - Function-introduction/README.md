
# Day 5 - Introduction to Python Functions

## 100 Days of Python Challenge

### Project: Personalized Greeting Generator

For Day 5 of my 100 Days of Python Challenge, I focused on learning how functions work in Python.

Instead of building a large project, I created a simple Personalized Greeting Generator to practice defining functions, passing arguments, and using parameters.

This project introduced an important programming concept that I will continue using throughout future challenges.

## Project Description

The Personalized Greeting Generator asks the user for their name and displays a customized welcome message.

The program also accepts the current challenge day as an argument, allowing the greeting to be reused for different days.

### Example Output

```text
What is your name? Chris
Hello, Chris, it's Day 5 of the challenge!
```

## Python Concepts Learned

### 1. Defining Functions

I learned how to create my own functions using the `def` keyword.

```python
def greet_user(name, day):
    print(f"Hello, {name}, it's Day {day} of the challenge!")
```

### 2. Parameters and Arguments

I learned that parameters are placeholders defined inside a function, while arguments are the actual values passed when calling the function.

```python
name = input("What is your name? ")
day = 5

greet_user(name, day)
```

### 3. Calling Functions

I learned that defining a function does not automatically execute it.

A function must be called before its code runs.

### 4. Using F-Strings

I practiced using f-strings to insert variables into printed messages.

## Challenges Encountered

One challenge I encountered was defining a function with two parameters but only passing one argument when calling it.

This caused an error because Python expected both arguments.

I corrected the problem by passing both `name` and `day` into the function.

## What I Learned

- How to define a function using `def`
- How to call a function
- The difference between parameters and arguments
- How to pass multiple arguments
- How to use f-strings inside functions
- Why functions make code reusable and organized

## How to Run

1. Make sure Python is installed.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

```bash
python greeting_generator.py
```

## Reflection

Day 5 was a shorter challenge, but it introduced one of the most important concepts in programming.

I initially struggled with passing multiple arguments into a function, but after correcting my mistake, I gained a better understanding of how functions receive information.

I can already see how functions will help organize larger programs.

## Next Steps

For Day 6, I plan to build an interactive text-based adventure game and use functions to organize different parts of the story.

---

**Day 5 Complete - 100 Days of Python Challenge**
