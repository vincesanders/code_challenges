class Solution:
    def isPalindrome(self, s: str) -> bool:
        # plan: loop forward and backward through string, to check if they match

        # make string with only alphanumeric chars
        newString = ''
        for i in range(len(s)):
            if s[i].isalnum():
                newString += s[i]

        if len(newString) == 0:
            return True
        
        forward = 0
        backward = len(newString) - 1

        while forward < len(newString) and backward > 0:
            if newString[forward].lower() == newString[backward].lower():
                forward += 1
                backward -= 1
                continue
            else:
                return False

        return True

s = "A man, a plan, a canal: Panama"

solution = Solution()

print(solution.isPalindrome(s))