class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        longestSubstring = 0

        if len(s) < 2:
            return len(s)

        letterCache = {}
        subStr = ''

        i = 0
        while i < len(s):
            char = s[i]
            if char not in letterCache:
                letterCache[char] = i
                subStr += char
                i += 1
            else:
                if len(subStr) > longestSubstring:
                    longestSubstring = len(subStr)
                i = letterCache[char] + 1
                letterCache = {}
                subStr = ''

        if len(subStr) > longestSubstring:
            longestSubstring = len(subStr)

        return longestSubstring