


import random
letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C',
'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']
print("Welcome to the PyPassword Generator!")
char_letters= int(input("How many letters would you like in your password?\n"))
char_symbols = int(input(f"How many symbols would you like?\n"))
char_numbers = int(input(f"How many numbers would you like?\n"))


#eazy

# password = ""
# for char in range(1, char_letters):
#     password += random.choice(letters)
# # print(password)

# for char in range(1, char_numbers):
#     password += random.choice(numbers)
# # print(password)

# for char in range(1, char_symbols):
#     password += random.choice(symbols)
# print(password)


#version 2


password_char = []
for char in range(1, char_letters):
 password_char += random.choice(letters)
# print(password)

for char in range(1, char_numbers):
    password_char += random.choice(numbers)
# print(password)

for char in range(1, char_symbols):
    password_char += random.choice(symbols)
print(password_char)


random.shuffle(password_char)
print(password_char)

password = ""
for char in password_char:
    password += char
print(password)