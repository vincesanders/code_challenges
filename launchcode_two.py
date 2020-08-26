#
# Complete the 'ChangeMaker' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. FLOAT price
#  2. FLOAT_ARRAY payment
#

def ChangeMaker(price, payment):
    # Write your code here
    # return array [1c, 5c, 10c, 25c]

    # initialize our return array with 0 change
    result = [0,0,0,0]

    # Edge case: no payment was entered
    if len(payment) <= 0:
        return result

    #initialize payment to 0
    total = 0
    # iterate through payment to get total
    for i in range(len(payment)):
        total += payment[i]

    #No money input, no change
    if total <= 0:
        return result

    # Make target an integer, so our values will be more valuable
    # Floats tend to be problematic, not giving exact values
    target = total * 100 - price * 100

    #Not enough money input
    if target < 0:
        # target will become the amount paid
        target = total * 100

    # Find highest possible coin for leftover total
    # keep iterating till all change has been figured
    while target > 0:
        if target >= 25:
            result[3] += 1
            target -= 25
        elif target >= 10:
            result[2] += 1
            target -= 10
        elif target >= 5:
            result[1] += 1
            target -= 5
        else:
            result[0] += 1
            target -= 1

    # return the change in the correct number of coins
    return result