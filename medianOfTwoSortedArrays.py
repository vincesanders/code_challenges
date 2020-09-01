from typing import List
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # iterate i, j, and k LIKE we're merging two sorted arrays, up to halfway point
        # once we get to midPoint - 1 and midPoint, reference current nums
        # after needed nums are reference, calculate median
        i = 0
        j = 0
        k = 0
        midNum = 0
        num2 = 0
        totalLength = len(nums1) + len(nums2)
        midIndex = (totalLength) // 2

        while k < midIndex + 2:
            if k == midIndex + 1:
                if totalLength % 2 == 0:
                    return (midNum + num2) / 2
                else:
                    
                    return float(midNum)
            if j >= len(nums2) or (i < len(nums1) and nums1[i] <= nums2[j]):
                if k == midIndex - 1:
                    num2 = nums1[i]
                elif k == midIndex:
                    midNum = nums1[i]
                i += 1
            else:
                if k == midIndex - 1:
                    num2 = nums2[j]
                elif k == midIndex:
                    midNum = nums2[j]
                j += 1
            k += 1

solution = Solution()

nums1 = []
nums2 = [1]

print(solution.findMedianSortedArrays(nums1, nums2))