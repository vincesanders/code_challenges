class Solution:
    def makeGood(self, s: str) -> str:
        i = 0
        while i < len(s) - 1:
            if s[i].islower() and s[i + 1] == s[i].upper():
                if i + 1 == len(s) - 1:
                    s = s[:len(s) - 2]
                    i = 0
                else:
                    s = s[:i] + s[i + 2:]
                    i = 0
            elif s[i].isupper() and s[i + 1] == s[i].lower():
                if i + 1 == len(s) - 1:
                    s = s[:len(s) - 2]
                    i = 0
                else:
                    s = s[:i] + s[i + 2:]
                    i = 0
            else:
                i += 1

        return s

solution = Solution()

s = "leEeetcode" # "leetcode"
s2 = "abBAcC" # ""
s3 = "s" # "s"
s4 = 'Pp' # ""
s5 = "hHcOzoC" # "cOzoC"

print(solution.makeGood(s))
print(solution.makeGood(s2))
print(solution.makeGood(s3))
print(solution.makeGood(s4))
print(solution.makeGood(s5))