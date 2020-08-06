import math
def solution(s, k):
    if k >= len(s):
        return 0
    shortest_length = math.inf
    for i in range(len(s) - k):
        right = i + k
        length = len(compress(s[:i] + s[right:]))
        if length < shortest_length:
            shortest_length = length
    return shortest_length

def compress(s): # O(n)
    char_count = 1
    output_string = ''
    for i in range(len(s)):
        if i < len(s) - 1 and s[i] == s[i + 1]:
            char_count += 1
        elif i > 0 and s[i] == s[i - 1]:
            output_string += str(char_count) + s[i]
            char_count = 1
        else:
            output_string += s[i]
    return output_string


s1 = "ABBBCCDDCCC"
s2 = "AAAAAAAAAAABXXAAAAAAAAAA"
s3 = "ABCDDDEFG"

print(solution(s1, 3))

print(solution(s2, 3))

print(solution(s3, 2))