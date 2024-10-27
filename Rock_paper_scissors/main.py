"""This is a ROCK, PAPER, SCISSORS game."""

# Import the variables file containing the icons
# and the random module for the computer's input
import random
import variables

# pylint: disable=anomalous-backslash-in-string
print('''       _                                         _
               | |                                       (_)
 _ __ ___   ___| | ___ __   __ _ _ __   ___ _ __ ___  ___ _ ___ ___  ___  _ __ ___
| '__/ _ \ / __| |/ / '_ \ / _` | '_ \ / _ \ '__/ __|/ __| / __/ __|/ _ \| '__/ __|
| | | (_) | (__|   <| |_) | (_| | |_) |  __/ |  \__ \ (__| \__ \__ \ (_) | |  \__ \
|_|  \___/ \___|_|\_\ .__/ \__,_| .__/ \___|_|  |___/\___|_|___/___/\___/|_|  |___/
                    | |         | |
                    |_|         |_|
''')

# Create a list of the imported variables
CHOICES = [variables.ROCK, variables.PAPER, variables.SCISSORS]

# Define variables for the possible outcomes
WIN_MESSAGE = "You win."
LOSE_MESSAGE = "You lose."
DRAW_MESSAGE = "It's a draw."

# Create a dictionary to store the results and
# map the user's input directly to the imported variables
OUTCOMES = {
    (0, 0): DRAW_MESSAGE, (0, 1): LOSE_MESSAGE, (0, 2): WIN_MESSAGE,
    (1, 0): WIN_MESSAGE, (1, 1): DRAW_MESSAGE, (1, 2): LOSE_MESSAGE,
    (2, 0): LOSE_MESSAGE, (2, 1): WIN_MESSAGE, (2, 2): DRAW_MESSAGE,
}

# Encapsulate the code in a while loop
# to perform error handling
while True:
    try:
        # Define the variable that will store the computer's choice
        COMPUTER_INPUT = random.choice(CHOICES)
        # Define the variable that will store the user's choice
        USER_INPUT = int(input("What do you choose?"
                               "Type 0 for Rock, 1 for Paper or 2 for Scissors: "))
        # Force the user to select 0, 1 or 2 with a conditional statement
        if USER_INPUT not in (0, 1, 2):
            print("Please enter 0 for Rock, 1 for Paper or 2 for Scissors: ")
            continue

        # Map user input to corresponding choice
        USER_CHOICE = CHOICES[USER_INPUT]
        print(f"User's choice: {USER_CHOICE}")
        print(f"Computer's choice: {COMPUTER_INPUT}")

        # Determine the result using the dictionary
        RESULT_MESSAGE = OUTCOMES[(USER_INPUT, CHOICES.index(COMPUTER_INPUT))]
        print(RESULT_MESSAGE)
        break  # Exit after printing the result
    except ValueError:
        print("Please enter 0 for Rock, 1 for Paper or 2 for Scissors: ")
