import math
# shortest subarray that contains all integers
def solution(a): # runtime: O(n), space: O(n)
    # add locations to a set
    minimum_days = math.inf
    destinations = set() # space: O(n)
    for i in range(len(a)): #O(n)
        if a[i] not in destinations:
            destinations.add(a[i])

    #sliding window
    left = 0
    right = 0

    while right < len(a):# O(2n) => O(n)
        test_array = a[left:right + 1]
        # check if all of the items is destinations are in the test array
        if destinations.issubset(test_array):
            #if true, see if the length of the current test array is shorter than current minimum
            if len(test_array) < minimum_days:
                minimum_days = len(test_array)
            # move the left pointer of the sliding window to try for a smaller minimum
            left += 1
        else:
            # if all destinations are not in the test array, 
            # expand the window by increasing right pointer
            right += 1

    return minimum_days

'''
improvements:
    Check for edgecases:
        No input (None or null) = throw type error
        empty array = result will be infinity
'''

print(solution(None))