'''
Smallest Substring of All Characters

Fiven an array of uique characters (arr) and a string (string), 
implement a function (getShortestUniqueSubstring) that 
finds the smallest substring of string containing all the charachters 
in arr. Return an empty string if such a substring doesn't exist
'''

def getShortestUniqueSubstring(a, s):
    a = set(a) # turn a into set
    substring = ''
    s = list(s)
    start = 0
    end = len(a)

    # find first substring
    while end < len(s) or start < len(s):
        if a.issubset(set(s[start:end])):
            substring = ''.join(s[start:end])
            #make the window smaller and start looking for smaller substring
            start += 1
        elif substring != '':
            # If we've already found a substring we are trying to beat
            # we can keep the window at a size smaller until we find a substring
            # with a smaller size of not
            start +=1
            if end < len(s):
                end += 1
        else:
            # This case only trigger until we find our first substring
            end += 1
    
    return substring

arr = ['x', 'y', 'z']
string = 'xyyzyzyx'

print(getShortestUniqueSubstring(arr, string))