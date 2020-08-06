'''
This algorithm assumes that the best strategy will always be to merge the smaller lists first.
'''
def solution(a):
    if len(a) < 2:
        return -1
    total_time = a[0] + a[1]
    a.sort()
    for i in range(1, len(a) - 1):
        if i < len(a) - 1:
            total_time += total_time + a[i + 1]

    return total_time

a = [100, 250, 1000, 1500]

print(solution(a))