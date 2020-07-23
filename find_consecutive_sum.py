'''
You're given an array with non-negative elements, find if the consecutive elements in the array will add up to the given value.

a = [4,6,4,5,7,9]

t = 100
t = 0
t = 9
'''

# sliding window
def consecutive_sum_exists(a, t):
    if t < 0:
        return False

    sum = 0

    for i in range(len(a)):
        j = 0
        while j < len(a) and sum < t:
            sum += a[j]
            j += 1
        if sum == t:
            return True

        sum -= a[i]

    return False