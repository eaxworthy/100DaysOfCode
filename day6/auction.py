import os

clear = lambda: os.system('clear')
bidders = {}

def get_bidder():
    name = input('What is your name?: ')
    bidders[name] = int(input('What is you bid??: $'))
    return input('Are there any other bidders? Type \'yes\' or \'no\'.\n')


print('Welcome to the secret auction program.')
more_bidders = 'yes'

while more_bidders == 'yes':
    more_bidders = get_bidder()
    clear()

clear()
winner = max(bidders, key=bidders.get)
print('The winner is ' + winner + f' with a bid of ${bidders[winner]}.')

