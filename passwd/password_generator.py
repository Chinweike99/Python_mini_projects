#!/usr/bin/python3
"""A Module that randomly generates Password"""

import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']

numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '/', '>', '<', '~']

print("\n\t\t\t\tWelcome to Password Generator!!\n")
n_letters = int(input("\t\t\tEnter number of letters: "))
n_numbers = int(input("\t\t\tEnter number of numbers: "))
n_symbols = int(input("\t\t\tEnter number of symbols: "))

password = []
for i in range(0, n_letters+1):
    char = random.choice(letters)
    password += char

for x in range(0, n_numbers + 1):
    char = random.choice(numbers)
    password += char

for y in range(0, n_symbols + 1):
    char = random.choice(symbols)
    password += char

print(f"\t\t\t{password}")
random.shuffle(password)
print(f"\t\t\t{password}")

pass_word = ""
for char in password:
    pass_word += char
print(f"\t\t\tYour password is: {pass_word}\n\n")
