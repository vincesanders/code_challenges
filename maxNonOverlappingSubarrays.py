#Not finished
from typing import List

class Solution:
    def maxNonOverlapping(self, nums: List[int], target: int) -> int:
        output = 0
        left = 0
        right = 0
        runningSum = 0
        while left < len(nums):
            if left == right:
                if nums[left] == target:
                    left += 1
                    if right < len(nums):
                        right += 1
                    output += 1
                else:
                    runningSum = nums[left]
                    if right < len(nums):
                        right += 1
                    else:
                        left += 1
            elif runningSum == target:
                if right < len(nums):
                    right = right + 1
                    left = right
                else:
                    left += 1
            elif right < len(nums) and runningSum + nums[right] == target:
                left = right + 1
                right = left
                runningSum = 0
                output += 1
            else:
                if right < len(nums):
                    runningSum += nums[right]
                # No current match
                # right or left needs to increment
                if runningSum > target: # we need subArray value to go down
                    if nums[left] > 0:
                        runningSum -= nums[left]
                        left += 1
                    elif right >= len(nums) - 1:
                        left += 1
                    else:
                        right += 1
                else:
                    # runningSum < target
                    if nums[left] < 0 and nums[right + 1] + runningSum != target:
                        left += 1
                        if left < len(nums):
                            runningSum -= nums[left]
                    elif right >= len(nums) - 1:
                        left += 1
                    else:
                        right += 1
        return output

arr = [1,1,1,1,1] # 2
arr2 = [-2,6,6,3,5,4,1,2,8] # 3
target = 2
target2 = 10 
solution = Solution()

print(solution.maxNonOverlapping(arr, target))
print(solution.maxNonOverlapping(arr2, target2))