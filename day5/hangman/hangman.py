import random
from lives import stages
import os
clear = lambda: os.system('clear')


word_list = ["aardvark", "baboon", "camel"]
word =random.choice(word_list)
life_count = 6
correct_guesses = ''

display = ['_' for i in range(len(word))]
print(word)

while '_' in display and life_count > 0:

    print(display)
    print(stages[life_count])

    guess = input('Please guess a letter: ').lower()
    clear()
    if not guess.isalpha() or len(guess) > 1:
        print('Please enter a single letter.')
    elif guess in correct_guesses:
        print('You\'ve already guessed \'' + guess + '\'. Try again')
    else:
        count = word.count(guess)
        if count:
            correct_guesses += guess
            while count > 0:
                ind = word.find(guess)
                display[ind] = guess
                count -= 1
                word = word[:ind] + '-' + word[ind + 1:]
        else:
            print(f'\'{guess}\' is not in the word.')
            life_count -= 1

if life_count:
    print(display, stages[life_count])
    print('You Win!')
else:
    print('You Lose.')
