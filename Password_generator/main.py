"""This is a password generator"""

# Import the random and string modules
import string
import random

# Define the project's variables
alphabet = list(string.ascii_lowercase)
special_symbols = ['!', '"', '$', '^']
numbers = list(string.digits)
password = []

# Greet the user
print("Welcome to the password generator!")

# Define the variables that will store the user's choices
nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

# Populate the password list with the number of
# letters chosen
for letter in range(nr_letters):
    password.append(random.choice(alphabet))

# Populate the password list with the number of
# symbols chosen
for symbol in range(nr_symbols):
    password.append(random.choice(special_symbols))

# Populate the password list with the number of 
# numbers chosen
for number in range(nr_numbers):
    password.append(random.choice(numbers))

# Shuffle around the contents of the list at random
password = random.sample(password, len(password))

# Display the resulting password 
print(f"Your password is: {''.join(password)}")
