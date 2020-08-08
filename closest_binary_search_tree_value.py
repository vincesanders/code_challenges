import math
# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def closestValue(self, root: TreeNode, target: float) -> int:
        return self.findClosetVal(root, target)[1]

    def findClosetVal(self, root, target, bestSoFar=(math.inf, None)):
        #bestSoFar is a tuple that contains, the value of the target - node.valu, and the node's value
        if root.val is None:
            pass
        elif abs(root.val - target) < bestSoFar[0]:
            bestSoFar = (abs(root.val - target), root.val)

        # node has already been evaluated
        # closeness should be measured by distance from 0 after node value - target
        if root.left is not None:
            bestSoFar = self.findClosetVal(root.left, target, bestSoFar)
        if root.right is not None:
            bestSoFar = self.findClosetVal(root.right, target, bestSoFar)

        return bestSoFar

bst = TreeNode(1, TreeNode(None), TreeNode(2))

solution = Solution()

print(solution.closestValue(bst, 3.428571))