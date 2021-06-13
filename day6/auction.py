import os

clear = lambda: os.system('clear')
bidders = {}

def get_bidder():
    name = input('What is your name?: ')
    bidders[name] = int(input('What is you bid??: $'))
    if input('Are there any other bidders? Type \'yes\' or \'no\'.\n')== 'yes':
        clear()
        get_bidder()


print('Welcome to the secret auction program.')
get_bidder()
clear()
print(bidders.get)
winner = max(bidders, key=bidders.get)
print('The winner is ' + winner + f' with a bid of ${bidders[winner]}.')

