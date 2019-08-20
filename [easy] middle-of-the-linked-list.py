# Given a non-empty, singly linked list with head node head, return a middle node of linked list.

# If there are two middle nodes, return the second middle node.

# Note:

# The number of nodes in the given list will be between 1 and 100.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def middleNode(self, head: ListNode) -> ListNode:
        idx = 1
        ans = head
        
        while head.next != None:
            head = head.next
            idx += 1
            if idx % 2 == 0:
                ans = ans.next
        
        return ans
