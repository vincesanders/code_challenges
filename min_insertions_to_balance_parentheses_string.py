class Solution:
    def minInsertions(self, s: str) -> int:
        stack = []
        insertions = 0
        # remove all matching parentheses
        i = 0
        while i < len(s):
            if len(stack) == 0 and s[i] == '(' or s[i] == '(':
                stack.append(s[i])
                i += 1
            elif i < len(s) -1 and s[i] + s[i + 1] == '))':
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                    i += 2
                else:
                    insertions += 1 # added (
                    i += 2
            else:
                # single )
                if len(stack) > 0 and stack[-1] == '(':
                    stack.pop()
                    insertions += 1
                    i += 1
                else:
                    insertions += 2
                    i += 1

        # deal with leftover stack
        # stack only contains (
        while len(stack) > 0:
            insertions += 2
            stack.pop()

        return insertions

solution = Solution()

s = "(()))"
s2 = "())"
s3 = "))())("
s4 = "(((((("
s5 = ")))))))"
s6 = "()())))()"

# print(solution.minInsertions(s))
# print(solution.minInsertions(s2))
# print(solution.minInsertions(s3))
# print(solution.minInsertions(s4))
# print(solution.minInsertions(s5))
print(solution.minInsertions(s6))