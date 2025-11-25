# Number Guessing Game

A simple number guessing game written in Python.

-----

## Description

This script implements a classic number guessing game. The player's goal is to guess a number randomly chosen between **1 and 100**.

  * The player starts with a **score of 100**.
  * For every incorrect guess, **10 points** are deducted from the score.
  * The score cannot go below **zero**.
  * After each guess, the program informs the player if their guess was "too high" or "too low."
  * If the player guesses the number correctly, their final score is displayed, and they are asked if they want to play again.

-----

## How to Run

You need **Python 3** (recommended) to run this game.

**1. Save the Code:**
Save the provided code in a file named `guess_number.py` or any name you prefer.

**2. Execute the Game:**
Open your terminal or command prompt, navigate to the directory where you saved the file, and run the following command:

```bash
python guess_number.py
```

-----

## How to Play

Follow the instructions below after running the script:

1.  The program will prompt you to enter your guess:
    ```
    Enter your guess between 1 and 100:
    ```
2.  Enter a number between **1 and 100** and press **Enter**.
3.  The program will give you feedback:
      * `You guessed too high!`
      * `You guessed too low!`
      * `You guessed correctly! Your score is: [Score]`
4.  To **quit** the game at any time, enter the letter `q` instead of a number and press Enter.

-----

## Key Functions

  * **`validate_input(input_num)`:**
      * Checks if the user input is a valid integer between 1 and 100.
      * Displays an appropriate error message and returns `False` if the input is invalid.
  * **`start_game()`:**
      * Contains the main game logic.
      * Generates a random number (`random.randint(1, 100)`).
      * Manages the main game loop, taking user input, validating it, responding to guesses, updating the score, and offering the option to play again.

-----

## Contribution

Suggestions or improvements to this simple code are welcome!
