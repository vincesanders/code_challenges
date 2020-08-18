# Definition for a binary tree node.
class TreeNode(object):
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution(object):
    def __init__(self):
        self.maxValue = float('-inf')
    def maximumAverageSubtree(self, root):
        """
        :type root: TreeNode
        :rtype: float
        """
        self.traverse(root)
        return self.maxValue
    
    def traverse(self, node):
        total = 0
        total += node.val
        numOfNodes = 1

        if node.left:
            leftAverage, numOfChildNodes, childTotal = self.traverse(node.left)
            numOfNodes += numOfChildNodes
            total += childTotal
            if leftAverage > self.maxValue:
                self.maxValue = leftAverage
        
        if node.right:
            rightAverage, numOfChildNodes, childTotal = self.traverse(node.right)
            numOfNodes += numOfChildNodes
            total += childTotal
            if rightAverage > self.maxValue:
                self.maxValue = rightAverage

        average = float(total) / numOfNodes
        if average > self.maxValue:
            self.maxValue = average

        return [average, numOfNodes, total]

solution = Solution()

root = TreeNode(2, None, TreeNode(1))

print(solution.maximumAverageSubtree(root))