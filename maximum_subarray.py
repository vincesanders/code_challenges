from typing import List

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sub_arr_num = nums[0]
        current_total = nums[0]
        
        for i in range(1, len(nums)):
            if current_total + nums[i] > nums[i]:
                current_total = current_total + nums[i]
            else:
                current_total = nums[i]

            if current_total < 0:
                current_total = nums[i]

            if current_total > max_sub_arr_num:
                max_sub_arr_num = current_total
        
        return max_sub_arr_num