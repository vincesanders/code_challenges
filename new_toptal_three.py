def solution(a, s): # runtime: O(n^2)
    # write your code in Python 3.6
    # naive solution (no time)
    result = 0
    for i in range(len(a)):
        total = a[i]
        if total == s:
            result += 1
        for j in range(i + 1, len(a)):
            total += a[j]
            if total / (j + 1 - i) == s:
                result += 1
        total = 0

    if result > 1000000000:
        return 1000000000
    else:
        return result

test = [[2, 1, 3], 2]
test2 = [[0, 4, 3, -1], 2]
test3 = [[2, 1, 4], 3]

print(solution(test[0], test[1]))
print(solution(test2[0], test2[1]))
print(solution(test3[0], test3[1]))