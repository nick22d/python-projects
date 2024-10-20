# A simple BMI calculator


# The variables storing the user supplied height and weight
height = float(input("What is your height? "))
weight = int(input("What is your weight? "))

# The formula calculating the user's BMI
bmi = weight / height ** 2

# Displaying to the user their calculated BMI
print("Your BMI is " + " " + str(bmi))
