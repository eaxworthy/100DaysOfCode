import random

choices =[ '''
    _______
---'   ____)
      (_____)
      (_____)
      (____)
---.__(___)
'''

, '''
    _______
---'   ____)____
          ______)
          _______)
         _______)
---.__________)
'''

, '''
    _______
---'   ____)____
          ______)
       __________)
      (____)
---.__(___)
'''
]
player_choice = int(input('What do you choose? Type 0 for Rock, 1 for Paper, or 2 for Scissors.\n'))
if player_choice not in [0,1,2,]:
    print('Fuck Off')
    exit()

comp_choice = random.randint(0,2)

print(choices[player_choice]+ '\nComputer Chose:\n'+ choices[comp_choice])

if player_choice-comp_choice in [1, -2]:
    print('You Win!')
elif player_choice-comp_choice == 0:
    print('Tie!')
else:
    print('You Lose.')
