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
                    if make_change(drinks[order]['cost']):
                        print(f'Here is your {order}. Enjoy!')
                        return { 'water': mr['water'] - drinks[order]['water'],
                                'coffee': mr['coffee'] - drinks[order]['coffee'],
                                'milk': mr['milk'] - drinks[order]['milk'],
                                'profit': mr['profit'] + drinks[order]['cost']
                                }
                else:
                    print('Sorry, there is not enough milk.')
            else:
                print('Sorry, there is not enough coffee.')
        else:
            print('Sorry, there is not enough water.')
    else:
        print('Invalid Order. Please try again.')
    return mr

def make_change(cost):
    '''Prompts user for money given in form of number of coins. Calculates
    total ammount of money, compares against price of drink, and reports
    value of change given back. Returns a value for the total ammount of
    money held in the machine'''
    print('Please insert coins.')
    quarters = int(input('How many quarters?: '))
    dimes = int(input('How many dimes?: '))
    nickles = int(input('How many nickles?: '))
    pennies = int(input('How many pennies?: '))
    total_given = quarters*0.25 + dimes*0.1 + nickles*0.05 + pennies*0.01
    if total_given >= cost:
        change_total = round(total_given - cost, 2)
        print(f'Here is ${change_total} dollars in change.')
        return True
    else:
        print('Sorry, insufficient change. Money refunded.')
        return False

def report():
    '''Return's a report on the current resources of the running coffee
    machine instance'''

    print(f"Water: {mr['water']}ml\nMilk: {mr['milk']}ml\nCoffee: {mr['coffee']}ml\nMoney: ${mr['profit']}")

on = True
print(drink_list)
while on:
    #valid inputs are one of the drinks or report
    order = input('What would you like? (espresso/latte/cappuccino): ')
    if order == 'report':
        report()
    elif order == 'off':
        on = False
    else:
        mr = process_order(order)
