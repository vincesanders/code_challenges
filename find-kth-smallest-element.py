'''
Given an array, find the kth smallest element.

A = {4,6,3,2,7}

k = 3
'''

# naive - sort array and then use index to fetck k
def find_kth_element(a, k): # Time: O(nlogn) Space: O(n) - timsort
    if a is None or len(a) is 0:
        raise ValueError("a must be an array containing at least one item.")
    if k > len(a) or k < 0:
        raise ValueError("k must be greater than 0 and less than the length of the array.")

    a.sort()

    return a[k - 1]

# more optimal? - min heap
from heapq import heappush, heappop
def find_kth_element_optimal(a, k): # Time: O(nlogn) Space: O(n) - timsort
    if a is None or len(a) is 0:
        raise ValueError("a must be an array containing at least one item.")
    if k > len(a) or k < 0:
        raise ValueError("k must be greater than 0 and less than the length of the array.")

    heap = []

    for i in range(len(a)):
        heappush(heap, a[i])

    for i in range(k - 1):
        heappop(heap)

    return heappop(heap)

a = [4,6,3,2,7]
k = 3

print(find_kth_element_optimal(a, k))