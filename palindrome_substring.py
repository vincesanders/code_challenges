# not finished
class Solution:
    def longestAwesome(self, s: str, checked=set()) -> int:
        if s in checked:
            # Do nothing
            return 0
        elif len(s) - len(set(s)) == len(s) // 2 or len(s) == 1:
            
            checked.add(s)
            # each number can only appear once or twice
            count = {}
            for c in s:
                if c in count:
                    count[c] += 1
                else:
                    count[c] = 1
            one = False
            for char in count:
                if count[char] % 2 != 0:
                    # invalid palindrome
                    return 0
                elif count[char] == 1:
                    if one:
                        return 0
                    else:
                        one = True
            return len(s)
        else:
            checked.add(s)
            romovedFromStart = self.longestAwesome(s[1:], checked)
            removedFromEnd = self.longestAwesome(s[:len(s) - 1], checked)

        return max(removedFromEnd, romovedFromStart)

s = "3242415" # 5
s2 = "12345678" # 1
s3 = "213123" # 6
s4 = "234121442" # 7

solution = Solution()

# print(solution.longestAwesome(s))
# print(solution.longestAwesome(s2))
# print(solution.longestAwesome(s3))
print(solution.longestAwesome(s4))