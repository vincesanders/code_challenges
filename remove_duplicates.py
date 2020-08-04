import re
class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        regex_repeats = '([a-z])\\1{' + str(k - 1) + '}'

        changed = True

        new_string = s

        while changed == True:

            compare_string = new_string

            new_string = re.sub(rf"{regex_repeats}", "", new_string)

            if compare_string == new_string:
                changed = False

        return new_string

solution = Solution()
s = "deeedbbcccbdaa"
print(solution.removeDuplicates(s, 3))