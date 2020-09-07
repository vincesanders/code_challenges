from typing import List

class Solution:
    def findItinerary(self, tickets: List[List[str]]) -> List[str]:
        if len(tickets) == 0:
            return []

        adjacencyList = {}

        # populate adjacency list
        for departure, destination in tickets: #O(n)
            if departure in adjacencyList:
                adjacencyList[departure].append(destination)
                adjacencyList[departure].sort(reverse=True)
            else:
                adjacencyList[departure] = [destination]

        # initialize the answer array
        itinerary = []
        #initialize stack with our starting airport
        stack = ['JFK']

        while len(stack) > 0:
            # get the airport at the top of the stack
            current = stack[len(stack) - 1]
            if current not in adjacencyList or len(adjacencyList[current]) == 0:
                # We've reached the end of this path, add current airport to itinerary
                itinerary.append(stack.pop())
                continue
            else:
                # Still airports to travel to, add to stack
                stack.append(adjacencyList[current].pop())

        return [airport for airport in reversed(itinerary)]

solution = Solution()

tickets = [["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]
tickets2 = [["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]
tickets3 = [["JFK","KUL"],["JFK","NRT"],["NRT","JFK"]]
tickets4 = [["EZE","TIA"],["EZE","HBA"],["AXA","TIA"],["JFK","AXA"],["ANU","JFK"],["ADL","ANU"],["TIA","AUA"],["ANU","AUA"],["ADL","EZE"],["ADL","EZE"],["EZE","ADL"],["AXA","EZE"],["AUA","AXA"],["JFK","AXA"],["AXA","AUA"],["AUA","ADL"],["ANU","EZE"],["TIA","ADL"],["EZE","ANU"],["AUA","ANU"]]

print(solution.findItinerary(tickets))
print(solution.findItinerary(tickets2))
print(solution.findItinerary(tickets3))
print(solution.findItinerary(tickets4))