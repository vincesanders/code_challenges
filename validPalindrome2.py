from math import ceil

class Solution:
    def validPalindrome(self, s):
        # check if the string in the given range is a palindrome
        def is_pali_range(start, end):
            for i in range(start, end):
                if s[i] != s[end - i + start]:
                    return False
            return True

        # loop through half the string
        for i in range(ceil(len(s) / 2)):
            # compare the char at the current index
            # to its corresponding indes at the end
            if s[i] != s[-i - 1]:
                # if we find 2 chars that don't match,
                # check if we will have a valid palindrome
                # if we remove one of the 2 chars
                end = len(s) - 1 - i
                return is_pali_range(i + 1, end) or is_pali_range(i, end - 1)
        
        return True