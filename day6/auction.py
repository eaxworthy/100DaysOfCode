import os

clear = lambda: os.system('clear')
bidders = {}

print('Welcome to the secret auction program.')
more_bidders = 'yes'

while more_bidders == 'yes':
    name = input('What is your name?: ')
    bidders[name] = int(input('What is you bid?: $'))
    more_bidders = input('Are there any other bidders? Type \'yes\' or \'no\'.\n')
    clear()

winner = max(bidders, key=bidders.get)
print('The winner is ' + winner + f' with a bid of ${bidders[winner]}.')

