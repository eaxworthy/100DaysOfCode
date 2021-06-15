import random
import os
from game_data import data

clear = lambda: os.system('clear')

def game():

    #assign the total number of entries in our data file to a variable
    total_cards = len(data)

    #create a random shuffling of our instagram personalities
    deck = random.sample(data, total_cards)

    score = 0

    while len(deck) > 1:
        card = deck.pop(0)
        a = card['follower_count']
        b = deck[0]['follower_count']
        print(f"A: {card['name']}, a {card['description']} from {card['country']}.")
        print("OR")
        print(f"B: {deck[0]['name']}, a {deck[0]['description']} from {deck[0]['country']}.")
        choice = input('Who has more followers? \'A\' or \'B\': ').lower()
        if (choice == 'a' and a > b) or (choice == 'b' and b > a):
            clear()
            score += 1
            print(f'You\'re right! Current score is {score}.')
        else:
            clear()
            print(f'Sorry, but that was incorrect. Your final score was {score}')
            return input('Play again?(y/n): ')
            exit()

    print(f'You guessed all {total_cards} entries right! Good Job!')

play = 'y'
while play == 'y':
    clear()
    play = game()
