print("Welcome to the Python Pizza Deliveries!")




while True:
    try: 
        size = str(input("What size pizza do you want? S, M or L: "))
        if size not in ("S", "M", "L"):
            print("Please choose S, M or L: ")
        else:
            if size == "S":
                size_fee = 15
            elif size == "M":
                size_fee = 20
            elif size == "L":
                size_fee = 25
            else:
                size_fee = 0
            break
    except ValueError:
        print("Please enter a valid size (i.e. S, M or L): ")

while True:
    try:
        pepperoni = str(input("Do you want pepperoni on your pizza? Y or N: "))
        if pepperoni not in ("Y", "N"):
            print("Please choose Y or N: ")
        else:
            if pepperoni == "Y" and size == "S":
                pepperoni_fee = 2
            elif pepperoni == "Y" and (size == "M" or size == "L"):
                pepperoni_fee = 3
            else: 
                pepperoni_fee = 0
            break
    except ValueError:
        print("Please choose 'Y' for 'yes' or 'N' for 'no': ")

while True:
    try:
        extra_cheese = str(input("Do you want extra cheese? Y or N: "))
        if extra_cheese not in ("Y", "N"):
            print("Please choose Y or N: ")
        else:
            if extra_cheese == "Y":
                cheese_fee = 1
            else:
                cheese_fee = 0
            break
    except ValueError:
        print("Please choose 'Y' for 'yes' or 'N' for 'no': ")


total_bill = size_fee + pepperoni_fee + cheese_fee

print(f"The total bill is {total_bill}")

