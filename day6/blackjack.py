
############### Our Blackjack House Rules #####################

## The deck is unlimited in size.
## There are no jokers.
## The Jack/Queen/King all count as 10.
## The the Ace can count as 11 or 1.
## Use the following list as the deck of cards:
## cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]
## The cards in the list have equal probability of being drawn.
## Cards are not removed from the deck as they are drawn.
## The computer is the dealer.

##################### Hints #####################

import random
import os

clear = lambda: os.system('clear')

cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

def deal():
    return random.sample(cards, 1)[0]

def sum_hand(hand):
    ace = 11 in hand
    total = sum(hand)
    if ace:
        if total > 21:
            total -= 10
        elif len(hand) == 2 and 10 in hand:
            return 0
    return total

def game():
    player_hand = random.sample(cards, 2)
    comp_hand = random.sample(cards, 2)
    comp_total = sum_hand(comp_hand)

    continue_game = 'h'
    while continue_game == 'h':
        print(f'Dealer\'s first card: [{comp_hand[0]}]')
        print(f'Your hand: {player_hand}')
        continue_game = input('Hit (h) or Pass (p)?: ')
        if continue_game == 'h':
            player_hand.append(deal())
            if comp_total < 17:
                comp_hand.append(deal())
                comp_total = sum_hand(comp_hand)

    player_total = sum_hand(player_hand)

    if player_total == 0:
        print('Player Wins!')
    elif comp_total == 0:
        print('Dealer Wins!')
    elif player_total <= 21:
        if player_total > comp_total:
            print('Player Wins!')
        elif player_total < comp_total and comp_total <= 21:
            print('Dealer Wins!')
        else:
            print('Tie!')
    else:
        if comp_total <= 21:
            print('Dealer Wins!')
        else:
            print('Tie!')
    return input('Would you like to play again?(y/n): ')

play = 'y'
while play == 'y':
    play = game()
    clear()
#Hint 1: Go to this website and try out the Blackjack game:
#   https://games.washingtonpost.com/games/blackjack/
#Then try out the completed Blackjack project here:
#   http://blackjack-final.appbrewery.repl.run

#Hint 2: Read this breakdown of program requirements:
#   http://listmoz.com/view/6h34DJpvJBFVRlZfJvxF
#Then try to create your own flowchart for the program.

#Hint 3: Download and read this flow chart I've created:
#   https://drive.google.com/uc?export=download&id=1rDkiHCrhaf9eX7u7yjM1qwSuyEk-rPnt

#Hint 4: Create a deal_card() function that uses the List below to *return* a random card.
#11 is the Ace.
#cards = [11, 2, 3, 4, 5, 6, 7, 8, 9, 10, 10, 10, 10]

#Hint 5: Deal the user and computer 2 cards each using deal_card() and append().
#user_cards = []
#computer_cards = []

#Hint 6: Create a function called calculate_score() that takes a List of cards as input
#and returns the score.
#Look up the sum() function to help you do this.

#Hint 7: Inside calculate_score() check for a blackjack (a hand with only 2 cards: ace + 10) and return 0 instead of the actual score. 0 will represent a blackjack in our game.

#Hint 8: Inside calculate_score() check for an 11 (ace). If the score is already over 21, remove the 11 and replace it with a 1. You might need to look up append() and remove().

#Hint 9: Call calculate_score(). If the computer or the user has a blackjack (0) or if the user's score is over 21, then the game ends.

#Hint 10: If the game has not ended, ask the user if they want to draw another card. If yes, then use the deal_card() function to add another card to the user_cards List. If no, then the game has ended.

#Hint 11: The score will need to be rechecked with every new card drawn and the checks in Hint 9 need to be repeated until the game ends.

#Hint 12: Once the user is done, it's time to let the computer play. The computer should keep drawing cards as long as it has a score less than 17.

#Hint 13: Create a function called compare() and pass in the user_score and computer_score. If the computer and user both have the same score, then it's a draw. If the computer has a blackjack (0), then the user loses. If the user has a blackjack (0), then the user wins. If the user_score is over 21, then the user loses. If the computer_score is over 21, then the computer loses. If none of the above, then the player with the highest score wins.

#Hint 14: Ask the user if they want to restart the game. If they answer yes, clear the console and start a new game of blackjack and show the logo from art.py.
