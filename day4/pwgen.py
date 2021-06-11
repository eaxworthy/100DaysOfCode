import random

letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

num_letters = int(input('Welcome to the PyPassword Generator!\nHow many letters would you like in your password?\n'))
num_numbers = int(input('How many numbers would you like?\n'))
num_symbols = int(input('How many symbols would you like?\n'))

chars = ''

for i in range(0, num_letters):
    chars+= letters[random.randint(0,25)]

for i in range(0, num_numbers):
    chars+= numbers[random.randint(0,9)]

for i in range(0,num_symbols):
    chars+=symbols[random.randint(0,8)]

password = ''.join(random.sample(chars, len(chars)))        
print(password)

