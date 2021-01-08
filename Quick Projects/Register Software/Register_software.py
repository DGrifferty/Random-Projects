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
    while change_required > 0:
        for denom in cash_present.keys():
            if change_required >= denom:
                change_required -= denom
                change_to_give.append(denom)
                break
    return change_to_give


def print_change_to_give(ctg):
    ctg.sort()
    instruction = ''
    for element in ctg:
        if element > 1:
            instruction += f'{ctg.count(element)} * £{element}'
            ctg[:] = [i for i in ctg if i != element]
            print(instruction)
        else:
            instruction += f'{ctg.count(element)} * {element * 100}p'
            ctg[:] = [i for i in ctg if i != element]

        if len(ctg) != 0:
            instruction += ', '

    return instruction


if __name__ == '__main__':
    denominations = [50, 20, 10, 5, 2, 1, 0.5, 0.2, 0.1, 0.05, 0.02, 0.01]
    cost = 20
    cash_present = generate_cash(denominations)

    print(cash_present)
    print(cash(cash_present, 10))

    print(print_change_to_give(cash(cash_present, 10)))
