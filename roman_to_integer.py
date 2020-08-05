class Solution:
    def romanToInt(self, s: str) -> int:
        # Create a dictionary to store roman numeral values
        roman_values = {
            'I': 1,
            'V': 5,
            'X': 10,
            'L': 50,
            'C': 100,
            'D': 500,
            'M': 1000,
        }

        # Track index and running total
        index = 0
        running_total = 0

        while index < len(s): # O(n)
            # set left to roman numeral at current index and right to the next
            left = roman_values[s[index]]
            # If we're at the end of the string, set right to 
            # equal the roman numeral at the current index
            right = roman_values[s[index + 1]] if index < len(s) - 1 else roman_values[s[index]]

            # If the left is greater than the right we can 
            # just add its value to the running total
            if left >= right:
                running_total += left
                index += 1
            # If right is greater that means we need to subtract left from the right value
            # This covers cases like IV (4) or CM (900)
            else:
                running_total += right - left
                index = index + 2

        return running_total

solution = Solution()

s = 'III'

print(solution.romanToInt(s))