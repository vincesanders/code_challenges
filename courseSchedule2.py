from typing import List
from collections import deque

class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        if len(prerequisites) == 0:
            return [i for i in range(numCourses)]

        adjacencyList = {}
        numPrereqs = {}
        for course, prereq in prerequisites:
            if prereq in adjacencyList:
                adjacencyList[prereq].append(course)
            else:
                adjacencyList[prereq] = [course]
            if course in numPrereqs:
                numPrereqs[course] += 1
            else:
                numPrereqs[course] = 1
        
        courseOrder = []

        # queue starts off with courses that don't have prereqs
        queue = deque([i for i in range(numCourses) if i not in numPrereqs])
        
        while len(queue) > 0:
            currentCourse = queue.popleft()
            courseOrder.append(currentCourse)
            if currentCourse in adjacencyList:
                for prereq in adjacencyList[currentCourse]:
                    # Knock off the num of prereqs, since we just finished one of prereqs
                    numPrereqs[prereq] -= 1

                    if numPrereqs[prereq] == 0:
                        queue.append(prereq)

        if len(courseOrder) == numCourses:
            return courseOrder
        else:
            return []


solution = Solution()

prereqs = [[1,0]]

print(solution.findOrder(2, prereqs))