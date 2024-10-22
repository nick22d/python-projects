# pylint: disable=anomalous-backslash-in-string
# Add ASCII art
print(r'''
                        |  ~~--.
                        |%=@%%/
                        |o%%%/
                     __ |%%o/
               _,--~~ | |(_/ ._
            ,/'  m%%%%| |o/ /  `\.
           /' m%%o(_)%| |/ /o%%m `\
         /' %%@=%o%%%o|   /(_)o%%% `\
        /  %o%%%%%=@%%|  /%%o%%@=%%  \
       |  (_)%(_)%%o%%| /%%%=@(_)%%%  |
       | %%o%%%%o%%%(_|/%o%%o%%%%o%%% |
       | %%o%(_)%%%%%o%(_)%%%o%%o%o%% |
       |  (_)%%=@%(_)%o%o%%(_)%o(_)%  |
        \ ~%%o%%%%%o%o%=@%%o%%@%%o%~ /
         \. ~o%%(_)%%%o%(_)%%(_)o~ ,/
           \_ ~o%=@%(_)%o%%(_)%~ _/
             `\_~~o%%%o%%%%%~~_/'
                `--..____,,--'

''')

# Greet the user
print("Welcome to the Python Pizza Deliveries!")

# Ask the user to choose their pizza SIZE
# while performing error handling as well
while True:
    try:
        SIZE = str(input("What SIZE pizza do you want? S, M or L: "))
        if SIZE not in ("S", "M", "L"):
            print("Please choose S, M or L: ")
        else:
            if SIZE == "S":
                SIZE_FEE = 15
            elif SIZE == "M":
                SIZE_FEE = 20
            elif SIZE == "L":
                SIZE_FEE = 25
            else:
                SIZE_FEE = 0
            break
    except ValueError:
        print("Please enter a valid SIZE (i.e. S, M or L): ")

# Ask the user to choose whether or not they
# want PEPPERONI on their pizza while
# performing error handling
while True:
    try:
        PEPPERONI = str(input("Do you want PEPPERONI on your pizza? Y or N: "))
        if PEPPERONI not in ("Y", "N"):
            print("Please choose Y or N: ")
        else:
            if PEPPERONI == "Y" and SIZE == "S":
                PEPPERONI_FEE = 2
            elif PEPPERONI == "Y" and SIZE in ("M", "L"):
                PEPPERONI_FEE = 3
            else:
                PEPPERONI_FEE = 0
            break
    except ValueError:
        print("Please choose 'Y' for 'yes' or 'N' for 'no': ")

# Ask the user to choose whether or not they
# want extra cheese on their pizza while
# performing error handling
while True:
    try:
        EXTRA_CHEESE = str(input("Do you want extra cheese? Y or N: "))
        if EXTRA_CHEESE not in ("Y", "N"):
            print("Please choose Y or N: ")
        else:
            if EXTRA_CHEESE == "Y":
                CHEESE_FEE = 1
            else:
                CHEESE_FEE = 0
            break
    except ValueError:
        print("Please choose 'Y' for 'yes' or 'N' for 'no': ")

# Calculate the total bill
TOTAL_BILL = SIZE_FEE + PEPPERONI_FEE + CHEESE_FEE

# Display to the user the total bill
print(f"The total bill is {TOTAL_BILL}")

