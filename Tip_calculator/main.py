


print("Welcome to the tip calculator!")

while True:
    try:
        total_bill = float(input("What was the total bill? $"))
        break
    except ValueError:
        print("Please provide your total bill in decimal format (i.e. 150.36)")

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

while True:
    try:
        people = int(input("How many people to split the bill? "))
        break
    except ValueError:
        print("Please provide a whole number (i.e. 5, 7, 10)")


individual_bill = round((total_bill + desired_tip) / people, 2)

print(f"Each person should pay: ${individual_bill}")