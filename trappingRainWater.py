from typing import List

class Solution:
    def trap(self, height: List[int]) -> int:
        waterTrapped = 0
        leftMaxArray = [] # stores the max left value at each index
        rightMaxArray = [0] * len(height) # stores the max right value at each index

        max = 0
        for i in range(len(height)): #O(n)
            if height[i] > max:
                max = height[i]
            leftMaxArray.append(max)

        max = 0
        i = len(height) - 1
        while i >= 0: #O(n)
            if height[i] > max:
                max = height[i]
            rightMaxArray[i] = max
            i -= 1

        # find the units of water at each index
        for i in range(len(height)): #O(n)
            waterAndGround = min(leftMaxArray[i], rightMaxArray[i]) # This is the level of the water at this index
            water = waterAndGround - height[i] # See how much water is above the ground
            if water > 0: # negative values mean there isn't any water at the index
                waterTrapped += water

        return waterTrapped

solution = Solution()

h = [0,1,0,2,1,0,1,3,2,1,2,1]

print(solution.trap(h))