"""This is a password generator"""

import string
import random

alphabet = list(string.ascii_lowercase)
special_symbols = ['!', '"', '$', '^']
numbers = list(string.digits)
password = []

print("Welcome to the password generator!")

nr_letters = int(input("How many letters would you like in your password? "))
nr_symbols = int(input("How many symbols would you like? "))
nr_numbers = int(input("How many numbers would you like? "))

for letter in range(nr_letters):
    password.append(random.choice(alphabet))

for symbol in range(nr_symbols):
    password.append(random.choice(special_symbols))

for number in range(nr_numbers):
    password.append(random.choice(numbers))

password = random.sample(password, len(password))

print("".join(password))
