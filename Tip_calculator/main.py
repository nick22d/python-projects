print("Welcome to the tip calculator!")
total_bill = float(input("What was the total bill? $"))
desired_tip = int(input("How much tip would you like to give? 10, 12, or 15? ")) / 100 * total_bill
people = int(input("How many people to split the bill? "))

individual_bill = round((total_bill + desired_tip) / people, 2)

print(f"Each person should pay: ${individual_bill}")
