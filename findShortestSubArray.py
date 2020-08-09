from typing import List
'''
Given a non-empty array of non-negative integers nums, the degree of this array is defined as the maximum frequency of any one of its elements.

Your task is to find the smallest possible length of a (contiguous) subarray of nums, that has the same degree as nums.
'''

class Solution:
    # first pass solution - time limit exceeded
    def findDegree(self, nums): # O(n)
        if len(nums) == 0:
            return 0
        
        repeats = {} 
        degree = 1

        for i in range(len(nums)):
            num = nums[i]
            if num in repeats:
                repeats[num] += 1
                if repeats[num] > degree:
                    degree = repeats[num]
            else:
                repeats[num] = 1
        
        return degree
    # first pass solution - time limit exceeded
    def findShortestSubArrayNaive(self, nums: List[int]) -> int:
        # get degree of nums
        degree = self.findDegree(nums)
        
        # find smallest subarray with that same degree
        # start window at full array size and walk it down as small as possible
        prev = 0
        # this loop will continue until the nums array wasn't changed during in iteration
        while len(nums) != prev: #O(n*2n)
            start = 0
            prev = len(nums)
            end = prev

            if self.findDegree(nums[:end - 1]) == degree: #O(n)
                end -= 1
                nums = nums[start:end]
            
            if self.findDegree(nums[start + 1:]) == degree: #O(n)
                start += 1
                nums = nums[start:end]

        return len(nums)

    def findShortestSubArray(self, nums: List[int]) -> int:
        start = {}
        end = {}
        repeats = {}

        for i in range(len(nums)): #O(n)
            if nums[i] not in start:
                # store first index of current number
                start[nums[i]] = i
            # store last index of current number
            end[nums[i]] = i
            #number of repeats
            if nums[i] not in repeats:
                repeats[nums[i]] = 0
            else:
                repeats[nums[i]] += 1

        length = len(nums)
        degree = max(repeats.values()) #O(n)
        for key in repeats:
            if repeats[key] == degree:
                length = min(length, end[key] - start[key] + 1)

        return length

solution = Solution()

arr = [1,2,2,3,1]
arr2 = [1,2,2,3,1,4,2]

print(solution.findShortestSubArray(arr))
print(solution.findShortestSubArray(arr2))