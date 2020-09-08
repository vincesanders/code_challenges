from typing import List
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def getSum(self, array):
        total = 0
        for i in range(len(array)):
            total += array[i]
        return total

    def findSumThisPath(self, root: TreeNode, total: int, path=[], solution=[]) -> List[List[int]]:
        if not root:
            return solution
        path.append(root.val)
        if root.left:
            pathCopy = [i for i in path]
            solution = self.findSumThisPath(root.left, total, pathCopy, solution)
        if root.right:
            pathCopy = [i for i in path]
            solution = self.findSumThisPath(root.right, total, pathCopy, solution)
        if not root.left and not root.right:
            # We're at a leaf
            if self.getSum(path) == total:
                # return solution with this path added
                solution.append(path)
        return solution

    def pathSum(self, root: TreeNode, total: int) -> List[List[int]]:
        return self.findSumThisPath(root, total, [], [])