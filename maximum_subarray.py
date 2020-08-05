from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # Initialize values with value at first index of nums
        # current_best tracks max found so far
        current_best = nums[0]
        # best_this_index tracks the best at the current index
        best_this_index = nums[0]
        
        for i in range(1, len(nums)):
            # Determine whether current number is better than the 
            # current number + the max of previous index
            if best_this_index + nums[i] > nums[i]:
                best_this_index = best_this_index + nums[i]
            # If current number is larger than adding the current 
            # number to previous index max, start a new subarray
            else:
                best_this_index = nums[i]

            # Is the max found at this index better than 
            # any other max we've found so far?
            if best_this_index > current_best:
                current_best = best_this_index
        
        return current_best