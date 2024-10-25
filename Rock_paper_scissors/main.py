"""This is a ROCK, PAPER, SCISSORS game."""

# Import the variables file containing the icons
# and the random module for the computer's input
import random, variables

# pylint: disable=anomalous-backslash-in-string
print('''
                _                                         _                        
               | |                                       (_)                       
 _ __ ___   ___| | ___ __   __ _ _ __   ___ _ __ ___  ___ _ ___ ___  ___  _ __ ___ 
| '__/ _ \ / __| |/ / '_ \ / _` | '_ \ / _ \ '__/ __|/ __| / __/ __|/ _ \| '__/ __|
| | | (_) | (__|   <| |_) | (_| | |_) |  __/ |  \__ \ (__| \__ \__ \ (_) | |  \__ \
|_|  \___/ \___|_|\_\ .__/ \__,_| .__/ \___|_|  |___/\___|_|___/___/\___/|_|  |___/
                    | |         | |                                                
                    |_|         |_|                                                
''')

CHOICES = [variables.ROCK, variables.PAPER, variables.SCISSORS]
WIN_MESSAGE = "You win."
LOSE_MESSAGE = "You lose."
DRAW_MESSAGE = "It's a draw."

while True:
    try:
        COMPUTER_INPUT = random.choice(CHOICES)
        USER_INPUT = int(input("What do you choose? Type 0 for Rock, 1 for Paper or 2 for Scissors: "))

        if USER_INPUT not in (0, 1, 2):
            print("Please enter 0 for Rock, 1 for Paper or 2 for Scissors: ")
            continue

        if USER_INPUT == 0:
            USER_INPUT = CHOICES[0]
        elif USER_INPUT == 1:
            USER_INPUT = CHOICES[1]
        elif USER_INPUT == 2:
            USER_INPUT = CHOICES[2]

        print(USER_INPUT)

        print(f"Computer chose: {COMPUTER_INPUT}")

        if USER_INPUT == CHOICES[0] and COMPUTER_INPUT == variables.ROCK:
            print(DRAW_MESSAGE)
            break
        elif USER_INPUT == CHOICES[0] and COMPUTER_INPUT == variables.PAPER:
            print(LOSE_MESSAGE)
            break
        elif USER_INPUT == CHOICES[0] and COMPUTER_INPUT == variables.SCISSORS:
            print(WIN_MESSAGE)
            break
        elif USER_INPUT == CHOICES[1] and COMPUTER_INPUT == variables.ROCK:
            print(WIN_MESSAGE)
            break
        elif USER_INPUT == CHOICES[1] and COMPUTER_INPUT == variables.PAPER:
            print(DRAW_MESSAGE)
            break
        elif USER_INPUT == CHOICES[1] and COMPUTER_INPUT == variables.SCISSORS:
            print(LOSE_MESSAGE)
            break
        elif USER_INPUT == CHOICES[2] and COMPUTER_INPUT == variables.ROCK:
            print(LOSE_MESSAGE)
            break
        elif USER_INPUT == CHOICES[2] and COMPUTER_INPUT == variables.PAPER:
            print(WIN_MESSAGE)
            break
        elif USER_INPUT == CHOICES[2] and COMPUTER_INPUT == variables.SCISSORS:
            print(DRAW_MESSAGE)
            break
    except ValueError:
        print("Please enter 0 for Rock, 1 for Paper or 2 for Scissors: ")
