total = float(input('Welcome to the tip calculator.\nWhat was the total bill? $'))
tip_rate = int(input('What percentage tip would you like to give? 10, 12, or 15? '))
num_people = int(input('How many people to split the bill? '))
print(f'Each person should pay: ${round((total+(total*(tip_rate/100)))/num_people,2):.2f}')
