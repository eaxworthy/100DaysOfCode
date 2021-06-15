from coffee_data import drinks, machine_resources

mr = machine_resources
drink_list = list(drinks.keys())

def process_order(order):
    '''Takes the drink order as a string, validates the option against
    available drinks, checks resources in running machine instance, and
    calculates change given back and new total of money in machine. Returns
    new state for machine resources'''

    if order in drink_list:
        if drinks[order]['water'] <= mr['water']:
            if drinks[order]['coffee'] <= mr['coffee']:
                if drinks[order]['milk'] <= mr['milk']:
                    new_money_total = make_change()
                    return { 'water': mr['water'] - drinks[order]['water'],
                            'coffee': mr['coffee'] - drinks[order]['coffee'],
                            'milk': mr['milk'] - drinks[order]['milk'],
                            'money': 0
                            }
                else:
                    print('Sorry, thee is not enough milk.')
            else:
                print('Sorry, thee is not enough coffee.')
        else:
            print('Sorry, thee is not enough water.')
    else:
        print('Invalid Order. Please try again.')
    return mr

def make_change():
    '''Prompts user for money given in form of number of coins. Calculates
    total ammount of money, compares against price of drink, and reports
    value of change given back. Returns a value for the total ammount of
    money held in the machine'''
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    total_given = round(quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01, 2)
    print(total_given)


def report():
    '''Return's a report on the current resources of the running coffee
    machine instance'''

    print(f"Water: {mr['water']}ml\nMilk: {mr['milk']}ml\nCoffee: {mr['coffee']}ml\nMoney: ${mr['money']}")

on = True
print(drink_list)
while on:
    #valid inputs are one of the drinks or report
    order = input('What would you like? (espresso/latte/cappuccino): ')
    if order == 'report':
        report()
    else:
        mr = process_order(order)
