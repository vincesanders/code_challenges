'''
Find the length of the longest non-repeating substring of a given string.
'''

string1 = 'aedfgaie'

def is_all_unique_char(string, start_index, end_index):
    char_set = set()
    for i in range(start_index, end_index):
        c = string[i]
        if c in char_set:
            return False
        else:
            char_set.add(c)
    return True

def longest_nonrepeating_String_Length_naive(string): # Time: O(n^3) Space: # O(n)
    if string is None or len(string) == 0:
        return 0

    max_length = 0

    for i in range(len(string)):
        for j in range(i + 1, len(string)):
            if is_all_unique_char(string, i, j):
                max_length = max_length if max_length > j - i else j - i

    return max_length

# sliding window
def longest_nonrepeating_String_Length(string):
    if string is None:
        return 0

    n = len(string)

    char_set = set()

    start = 0
    end = 0
    max_length = 0

    while start < n and end < n:
        char = string[end]
        if char not in char_set:
            char_set.add(char)
            end += 1
            max_length = max_length if max_length > end - start else end - start
        else:
            char_set.remove(string[start])
            start += 1
    return max_length

print(longest_nonrepeating_String_Length_naive(string1))