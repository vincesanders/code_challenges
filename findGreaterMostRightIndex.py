'''
Input a = [21,5,6,56,88,52], output = [5,5,5,4,-1,-1] . Output array values is made up of indices of the element with value greater than the current element but with largest index. So 21 < 56 (index 3), 21 < 88 (index 4) but also 21 < 52 (index 5) so we choose index 5 (value 52). Same applies for 5,6 and for 56 its 88 (index 4). If there is no greater element then use -1 and last element of the array will always have value of -1 in output array since there is no other elment after it. Follow up to consider the input as a stream, how can we only update smaller element (use specific Data structure), running time and space complexity discussion.
'''
def find_greater_most_right_index_naive(nums):
    result = [-1] * len(nums)

    for i in range(len(nums)):
        for j in range(i + 1, len(nums)):
            if nums[j] > nums[i]:
                result[i] = j
    
    return result

from heapq import heappush, heappop

def find_greater_most_right_index(nums):
    heap = []

    # Add values to heap in the form of a tuple (-(value), index)
    for i, value in enumerate(nums):
        # sort by negative value at current index
        # we want the highest numbers to be at the top of our minheap
        heappush(heap, (-value, i))
    
    # build result array with intitial values of -1 (no greater value found)
    result = [-1] * len(nums)
    maxIndex = -1

    # iterate till heap is empty
    while heap:
        current = heappop(heap) # current is a tuple
        currentIndex = current[1]

        # if current index is more than max index or the value at the 2 indexes is equal
        if currentIndex > maxIndex or nums[maxIndex] == nums[currentIndex]:
            # max index becomes the higher of the 2
            maxIndex = max(currentIndex, maxIndex)
            continue

        # else we add the max index to our result at the current index
        result[currentIndex] = maxIndex
        maxIndex = max(currentIndex, maxIndex) # set new maxIndex value
        
    return result

nums = [21,5,6,56,88,52] # [5,5,5,4,-1,-1]

print(find_greater_most_right_index_naive(nums))

print(find_greater_most_right_index(nums))