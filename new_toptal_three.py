def solution(a, s): # runtime: O(n^2) space: O(1)
    # write your code in Python 3.6
    # naive solution (no time)
    result = 0
    for i in range(len(a)): #O(n^2)
        # initialize total with value at i
        total = a[i]
        # if a[i] by itself is equal to s, increment result
        # because the avg of a single value will be itself
        if total == s:
            result += 1
        
        # Look for other subarrays starting at i whose averages will match s 
        for j in range(i + 1, len(a)):
            total += a[j]
            if total / (j + 1 - i) == s:
                result += 1
        total = 0 # don't need

    # this case was included in the description
    # if the result is over 1 mil, return 1 mil
    if result > 1000000000:
        return 1000000000
    else:
        return result

'''
improvements:
    Check for edgecases:
        No array or s value
        empty array = result will infinity
    Check for over 1 mil as adding up result in main loop? 
        it could optimize on a large input,
        but it would be an extra operation on smaller inputs
'''

test = [[2, 1, 3], 2]
test2 = [[0, 4, 3, -1], 2]
test3 = [[2, 1, 4], 3]

print(solution(test[0], test[1]))
print(solution(test2[0], test2[1]))
print(solution(test3[0], test3[1]))