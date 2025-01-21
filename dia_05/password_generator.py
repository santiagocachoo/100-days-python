#Password Generator Project
import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

print("Welcome to the PyPassword Generator!")
nr_letters= int(input("How many letters would you like in your password? ")) 
nr_symbols = int(input(f"How many symbols would you like? "))
nr_numbers = int(input(f"How many numbers would you like? "))

#Eazy Level - Order not randomised:
#e.g. 4 letter, 2 symbol, 2 number = JduE&!91
"""
password = ""

# letters
for n in range(1, nr_letters + 1):
    password += random.choice(letters)

# symbols
for n in range(1, nr_symbols + 1):
    password += random.choice(symbols)

# numbers 
for n in range(1, nr_numbers + 1):
    password += random.choice(numbers)

print(password)

"""

#Hard Level - Order of characters randomised:
#e.g. 4 letter, 2 symbol, 2 number = g^2jk8&P

password_list = []

# letters
for n in range(1, nr_letters + 1):
    password_list += random.choice(letters)

# symbols
for n in range(1, nr_symbols + 1):
    password_list += random.choice(symbols)

# numbers 
for n in range(1, nr_numbers + 1):
    password_list += random.choice(numbers)

# shuffle password list
random.shuffle(password_list)

# turn character list to string and print
password = "".join(password_list)
print(password)
        