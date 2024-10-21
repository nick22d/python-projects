# Initialise the variables
height = None
weight = None

# Ask the user to supply their height in centimeters which is then
# converted into a decimal number representing meters
while True:
    try:
        height = float(input("What is your height in centimeters? "))
        real_height = height / 100
        break
    except ValueError:
        print("Please enter a valid value (i.e. 176): ")

# Ask the user to supply a whole number representing their weight        
while True:
    try:
        weight = int(input("What is your weight in kilograms? "))
        break
    except ValueError:
        print("Please enter a whole number (i.e. 80): ")

# Calculate the user's BMI while rounding the result
# to 2 decimal places
bmi = round((weight / real_height ** 2), 2)

# Display to the user their BMI
print(f'Since your height is {real_height}m and your weight is {weight}kg, your BMI is {bmi}.')

