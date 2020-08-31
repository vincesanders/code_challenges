from typing import List

class Solution:
    def threeSum(self, arr: List[int]) -> List[List[int]]:
        # Write your code here
        triplets = []
        tripletsSet = set()

        # sort the array so we can say with certainty we've checked all
        # values, when using a 'meeting in the middle strategy'.
        # If I could do this again, knowing I would have the time, 
        # I would have implemented an in-place merge sort, to bring time complexity down to O(1)
        arr.sort() # O(nlogn) Space: O(n)

        # iterate through the array.
        # for each item in the array, we're going to be checking the other items in the array
        # for a match
        # in order to avoid n^2 or n^3 runtime, we're going to use a "meet in the middle" strategy
        for i in range(len(arr) - 2): # O((n^2) / 2) -> O(n^2)
            # second number index
            # we don't need to check the current number against numbers before it,
            # because the array is sorted and we've already checked those numbers against
            # the current

            #set the low pointer to the index after the current index
            low = i + 1

            # third number index
            #Set the high pointer to the last index in the array
            high = len(arr) - 1

            # check for matches
            while low < high:

                # using "is" caused an error on 4th test case (large numbers?)
                if arr[i] + arr[low] + arr[high] == 0:
                    # triplet found
                    triplet = (arr[i], arr[low], arr[high])
                    if triplet not in tripletsSet:
                        triplets.append(list(triplet))
                        tripletsSet.add(triplet)
                    # increment and decrement low and high values and look for other matches.
                    low += 1
                    high -= 1

                elif arr[i] + arr[low] + arr[high] < 0:
                    # no match was found and we're not reaching the target
                    low += 1
                else:
                    # no match was found and we're adding up to higher than the target
                    high -= 1

        return triplets

solution = Solution()

nums = [-1,0,1,2,-1,-4]

print(solution.threeSum(nums))