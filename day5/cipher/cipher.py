#letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z']]

letters ='abcdefghijklmnopqrstuvwxyz'

def caesar(message, shift_num, mode):
    result = ''
    if mode == 'decode':
        shift_num *= -1
    for char in message:
        if char.isalpha():
            c = letters[(letters.find(char.lower())+ shift_num)%26]
            result += c
        else:
            result += char
    return result

def main():
    mode = input('Type \'encode\' to encrypt, type \'decode\' to decrypt:\n').lower()

    while mode not in ['encode', 'decode']:
        mode = input('Invalid Option Selected. Enter \'encode\' or \'decode\': ')

    message = input('Type your message:\n')

    shift_num = int(input('Type the shift number:\n'))

    print('Here is the ' + mode +'ed result: ' + caesar(message, shift_num, mode))
    if input('Would you like to continue?(y/n): ') == 'y':
        main()

main()
