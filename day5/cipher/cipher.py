#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]

letters ='abcdefghijklmnopqrstuvwxyz'

def encrypt(message, shift_num):
    result = ''
    for char in message:
        if char.isalpha():
            c = letters[(letters.find(char.lower())+ shift_num)%26]
            result += c
        else:
            result += char
    return result

def decrypt(message, shift_num):
    result = ''
    for char in message:
        if char.isalpha():
            c = letters[(letters.find(char.lower()) - shift_num)%26]
            result += c
        else:
            result += char
    return result


option = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n').lower()

while option not in ['encode', 'decode']:
    option = input('Invalid Option Selected. Enter \'encode\' or \'decode\': ')

message = input('Type your message:\n')

shift_num = int(input('Type the shift number:\n'))

if option == 'encode':
    print('Here is the encoded result: ' + encrypt(message, shift_num))
else:
    print('Here is the decoded result: ' + decrypt(message, shift_num))



