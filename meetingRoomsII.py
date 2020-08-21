from heapq import heappush, heappop
from typing import List

class Solution:
    def minMeetingRooms(self, intervals: List[List[int]]) -> int:
        if intervals is None or len(intervals) == 0:
            return 0

        # use timsort to sort meetings by start times
        intervals.sort() #O(nlogn)

        heap = []
        #heappush(heap, (arr[1], arr0))
        # heappush will sort based on the first value, so 
        # we're converting the values into a tuple with the endtime first.
        heappush(heap, (intervals[0][1], intervals[0][0]))

        for i in range(1, len(intervals)): #O(n)
            # get current meeting
            currentMeeting = intervals[i]
            # get earliest meeting from heap
            earliestMeeting = heappop(heap)
            # if no time conflict - current meeting starts afer or at same time earlist meeting ends
            if currentMeeting[0] >= earliestMeeting[0]:
                # make the current meeting the new earliest meeting and add it to heap (below)
                earliestMeeting = (currentMeeting[1], currentMeeting[0])
            else:
                # if times DO conflict, we'll have to add a new meeting to the heap
                heappush(heap, (currentMeeting[1], currentMeeting[0]))

            heappush(heap, earliestMeeting)

        # The answer will be the same as the amount of meetings still in the heap.
        return len(heap)