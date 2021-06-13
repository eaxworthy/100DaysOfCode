import random

number = random.randint(1,100)
print('I\'m thinking of a number beween 1 and 100.')
mode = ''

while mode not in ['easy', 'hard']:
    mode = input('Choose a difficulty. Type \'easy\' or \'hard\': ')

if mode == 'easy':
    attempts = 10
else:
    attempts = 5

while attempts:
    print(f'You have {attempts} attempts left to guess the number.')
    guess = int(input('Make a guess: '))
    if guess == number:
        print(f'You win! The number was {number}.')
        exit()
    elif guess > number:
        print('Too high.')
    else:
        print('Too low.')
    attempts -= 1
    if attempts:
        print('Guess again.\n')
    else:
        print('You\'ve run out of guesses, you lose.')
