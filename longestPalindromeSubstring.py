class Solution:
    def findPalindromeLength(self, s, left, right): # time: O(n) space: O(1)
        if s is None or left > right: return 0

        # keep expanding out till we can't expand anymore
        # or until our palindrome is broken
        while left >= 0 and right < len(s) and s[left] == s[right]:
            left -= 1
            right += 1

        return right - left - 1
    
    def longestPalindrome(self, s: str) -> str: # time: O(n^2) space: O(1)
        if s is None or len(s) < 1: return ''

        start = 0
        end = 0

        # iter through s, trying to find pali by expanding out from i
        for i in range(len(s)): # O(n)
            # handle case of palindrome with single middle char - racecar
            oddPali = self.findPalindromeLength(s, i, i) #O(n)
            # handle normal palindrome - teet
            evenPali = self.findPalindromeLength(s, i, i + 1) #O(n)
            LongestPali = max(oddPali, evenPali)

            if LongestPali > end - start:
                # i is the middle char
                start = i - (LongestPali - 1) // 2
                end = i + LongestPali // 2

        print(start)
        print(end)

        return s[start:end + 1]

solution = Solution()

print(solution.longestPalindrome('babad'))
