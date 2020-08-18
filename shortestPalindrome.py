class Solution:
    def shortestPalindrome(self, s: str) -> str:
        # use Knuth-Morris-Pratt find substring algo
        #    string + # + string reversed
        if s is None or s == "":
            return ''
        sCopy = s + '#' + s[::-1]

        start = 0
        end = 1
        pattern = [None] * len(sCopy)

        while end < len(sCopy):
            if sCopy[start] == sCopy[end]:
                pattern[end] = start
                start += 1
                end += 1
            elif start > 0 and pattern[start - 1] is not None:
                start = pattern[start - 1] + 1
            elif start > 0:
                start = 0
            else:
                end += 1
        
        index = -1
        while pattern[index] == None:
            index -= 1
        
        maxCommonLength = pattern[index] + 1
        return s[::-1][:-maxCommonLength] + s



solution = Solution()

s = "aacecaaa"
s2 = "abcd"
s3 = "aabba"

print(solution.shortestPalindrome(s))
print(solution.shortestPalindrome(s2))
print(solution.shortestPalindrome(s3))