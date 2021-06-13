def calculate(a, b, mode):
    res = 0
    if mode == '+':
        res = a + b
    elif mode == '-':
        res = a - b
    elif mode == '*':
        res = a * b
    else:
        res = a / b
    print(f'The result of {a} {mode} {b} is {res}.')
    return res

def calculator():
    a = float(input('What\'s the first number?: '))
    print('+\n-\n*\n\\')
    continue_calc = 'y'
    while continue_calc == 'y':
        mode = input('Pick an operation: ')
        b = float(input('What\'s the second number?: '))
        a = calculate(a, b, mode) 
        continue_calc = input(f'Would you like to continue calculations with {a}?(y/n) : ')
    
calculator()
