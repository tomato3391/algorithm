# Given a linked list, reverse the nodes of a linked list k at a time and return its modified list.

# k is a positive integer and is less than or equal to the length of the linked list. If the number of nodes is not a multiple of k then left-out nodes in the end should remain as it is.

# Note:

# Only constant extra memory is allowed.
# You may not alter the values in the list's nodes, only nodes itself may be changed.

# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, x):
#         self.val = x
#         self.next = None

class Solution:
    def reverseKGroup(self, head: ListNode, k: int) -> ListNode:
        if head is None:
            return None
        ans = None
        tmp = head
        length = 0
        
        while tmp is not None:
            length += 1
            tmp = tmp.next
            
        cur = head
        stack = []
        
        import copy
        for i in range(int(length / k)):
            for i in range(k):
                node = ListNode(cur.val)
                stack.append(node)
                cur = cur.next
                    
            while len(stack) > 0:
                if tmp is None:
                    tmp = stack.pop()
                    ans = tmp
                else:
                    tmp.next = stack.pop()
                    tmp = tmp.next
        if ans is None:
            return cur
        
        tmp.next = cur
        
        return ans
