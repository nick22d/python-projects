"""This is a program that calculates one's BMI."""

# Initialise the variables
HEIGHT = None
WEIGHT = None

# Ask the user to supply their HEIGHT in centimeters which is then
# converted into a decimal number representing meters
while True:
    try:
        HEIGHT = float(input("What is your HEIGHT in centimeters? "))
        real_HEIGHT = HEIGHT / 100
        break
    except ValueError:
        print("Please enter a valid value (i.e. 176): ")

# Ask the user to supply a whole number representing their WEIGHT
while True:
    try:
        WEIGHT = int(input("What is your WEIGHT in kilograms? "))
        break
    except ValueError:
        print("Please enter a whole number (i.e. 80): ")

# Calculate the user's BMI while rounding the result
# to 2 decimal places
bmi = round((WEIGHT / real_HEIGHT ** 2), 2)

# Display to the user their BMI
print(f"Since your HEIGHT is {real_HEIGHT}m and your WEIGHT is {WEIGHT}kg, your BMI is {bmi}.")

