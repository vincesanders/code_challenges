import math
# shortest subarray that contains all integers
def solution(a):
    # add locations to a set
    minimum_days = math.inf
    destinations = set()
    for i in range(len(a)):
        if a[i] not in destinations:
            destinations.add(a[i])

    #sliding window?
    left = 0
    right = 0

    while right < len(a):
        test_array = a[left:right + 1]
        if destinations.issubset(test_array):
            if len(test_array) < minimum_days:
                minimum_days = len(test_array)
            left += 1
        else:
            right += 1

    return minimum_days


    # destinations..issubset()