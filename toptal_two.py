import math

def solution(s, x, y):
    points = {}
    max_distance = math.inf
    count = 0

    for i in range(len(s)):
        distance = x[i] * x[i] + y[i] * y[i]
        if s[i] in points:
            max_distance = distance
        else:
            points[s[i]] = distance

    for p in points:
        if points[p] < max_distance:
            count += 1

    return count


s1 = "ABDCA"
x1 = [2,-1,-4,-3,3]
y1 = [2,-2,4,1,-3]

s2 = "ABB"
x2 = [1,-2,-2]
y2 = [1,-2,2]

s3 = "CCD"
x3 = [1,-1,2]
y3 = [1,-1,-2]

print(solution(s1, x1, y1))
print(solution(s2, x2, y2))
print(solution(s3, x3, y3))