from typing import List
class Solution:
    def findMin(self, nums: List[int]) -> int:
        lastIndex = None
        for i in range(len(nums) - 1):
            if nums[i] > nums[i + 1]:
                lastIndex = i
                break

        if lastIndex is None:
            # the array is not rotated.
            return nums[0]
        else:
            return nums[lastIndex + 1]