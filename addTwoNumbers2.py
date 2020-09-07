# Definition for singly-linked list.
class ListNode:
    def __init__(self, val=0, next=None):
        self.val = val
        self.next = next
class Solution:
    def linkedListToString(self, ll):
        string = ''
        current = ll
        while current is not None:
            string += str(current.val)
            current = current.next
        return string
    
    def addTwoNumbers(self, l1: ListNode, l2: ListNode) -> ListNode:
        # iterate through each ll, converting to a string representing the number
        # Add the 2 numbers, then convert them back to a string
        finalNum = str(int(self.linkedListToString(l1)) + int(self.linkedListToString(l2)))

        # The first node will be a throw-away node
        newList = ListNode()
        current = newList

        # Build the new Linked list from the string
        for i in range(len(finalNum)):
            current.next = ListNode(int(finalNum[i]))
            current = current.next

        return newList.next

