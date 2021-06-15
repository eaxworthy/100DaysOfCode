import random
from game_data import data

#assign the total number of entries in our data file to a variable
total_cards = len(data)

#create a random shuffling of our instagram personalities
deck = random.sample(data, total_cards)

choice = deck.pop()
print(choice['name'] + ' ' + deck[0]['name'])
