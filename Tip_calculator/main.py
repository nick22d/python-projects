# pylint: disable=anomalous-backslash-in-string
# Add ASCII art
print('''
 _____________________
|  _________________  |
| | JO           0. | |
| |_________________| |
|  ___ ___ ___   ___  |
| | 7 | 8 | 9 | | + | |
| |___|___|___| |___| |
| | 4 | 5 | 6 | | - | |
| |___|___|___| |___| |
| | 1 | 2 | 3 | | x | |
| |___|___|___| |___| |
| | . | 0 | = | | / | |
| |___|___|___| |___| |
|_____________________|
''')

# Greet the user.
print("Welcome to the tip calculator!")

# Ask the user for their total bill in the form of
# a decimal number and perform error handling.
while True:
    try:
        total_bill = float(input("What was the total bill? $"))
        break
    except ValueError:
        print("Please provide your total bill in decimal format (i.e. 150.36)")

# Ask the user for their desired tip and ensure that it's either
# 10 or 12 or 15. Also handle errors accordingly.
while True:
    try:
        tip = int(input("How much tip would you like to give? 10, 12, or 15? "))
        if tip not in (10, 12, 15):
            print("Please choose a tip from the following values: 10, 12, 15: ")
        else:
            desired_tip = tip / 100 * total_bill
            break
    except ValueError:
        print("Please choose a tip from the following values: 10, 12, 15: ")

# Ask the user for the number of participants amongst
# whom the bill will be split.
while True:
    try:
        people = int(input("How many people to split the bill? "))
        break
    except ValueError:
        print("Please provide a whole number (i.e. 5, 7, 10)")

# Calculate the individual bill that everybody will have to pay.
individual_bill = round((total_bill + desired_tip) / people, 2)

# Display to the user the individual bill.
print(f"Each person should pay: ${individual_bill}")