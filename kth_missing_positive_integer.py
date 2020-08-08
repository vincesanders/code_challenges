from typing import List
class Solution:
    def findKthPositive(self, arr: List[int], k: int) -> int:
        missing = []
        numCheck = 1
        i = 0
        foundKth = False
        while not foundKth:
            if i < len(arr) and arr[i] == numCheck:
                # We've found our expected number
                i += 1
                numCheck += 1
            else:
                missing.append(numCheck)
                numCheck +=1
                if len(missing) == k:
                    foundKth = True
                    return missing[-1]

arr = [2,3,4,7,11]
arr2 = [1,2,3,4]
k2 = 2

k = 5

solution = Solution()

print(solution.findKthPositive(arr2, k2))