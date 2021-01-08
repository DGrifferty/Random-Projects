import random


# in progress

def generate_cash(denominations):
    cash_present = {}
    for denom in denominations:
        if 5 < denom <= 10:
            cash_present[denom] = int(100 / denom)
        if 1 < denom <= 5:
            cash_present[denom] = int(10 / denom)
        else:
            cash_present[denom] = int(1 / denom)
    return cash_present


def cash(cash_present, change_required):
    change_to_give = []
    change_required = int(change_required * 1000)
    while change_required != 0:
        for denom in cash_present.keys():
            if change_required >= denom * 1000:
                change_required -= denom * 1000
                change_to_give.append(denom)
                cash_present[denom] -= 1
                break
    return change_to_give, cash_present


def gen_change_instructions(ctg):
    ctg.sort(reverse=True)
    print(ctg)
    instruction = ''
    while len(ctg) != 0:
        for element in ctg:
            if element >= 1:
                instruction += f'{ctg.count(element)} * £{element}'
                ctg[:] = [i for i in ctg if i != element]
                if len(ctg) != 0:
                    instruction += ', '
                break
            else:
                instruction += f'{ctg.count(element)} * {element * 100}p'
                ctg[:] = [i for i in ctg if i != element]
                if len(ctg) != 0:
                    instruction += ', '
                break

    return instruction


if __name__ == '__main__':
    denominations = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    payed = True
    cash_present = generate_cash(denominations)
    while True:
        if payed:
            cost = random.randint(1, 10000) / 100.0
            print(f'Cost {cost}')
            payed = False

        option = input('How would you like to pay?\n1. Cash\n2. Card\n3. Both\n:').lower()

        if '/' in option:
            if option == '/exit':
                quit()
            elif option == '/help':
                print('help message')
            else:
                print('Unknown command')

        if option == '1':
            while not payed:
                try:
                    cash_given = float(input('Enter cash given: '))
                    if cash_given == round(cost, 2):
                        print('Payed.')
                        payed = True
                        break
                    elif cash_given > cost:
                        change_required = round(cash_given - cost, 2)
                        change_to_give, cash_present = cash(cash_present, change_required)
                        print(f'Change required = £{change_required}')
                        print(gen_change_instructions(change_to_give))
                        payed = True
                        break
                    else:
                        print('Insufficient, give more cash')
                except:
                    print('Enter a number.')
        elif option == '2':
            print('Payed')  # Could make this work with banking software
            payed = True
        elif option == '3':
            while not payed:
                try:
                    cash_given = int(input('Enter cash given: '))
                    cost -= cash_given
                    print(f'£{cost} payed by card')
                    payed = True
                except:
                    print('Enter a number.')
        else:
            print('Option not present')
