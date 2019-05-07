# Given a Binary Search Tree (BST) with the root node root, return the minimum difference between the values of any two different nodes in the tree.
# Note:
# The size of the BST will be between 2 and 100.
# The BST is always valid, each node's value is an integer, and each node's value is different.

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:
    pre = -float('inf')
    res = float('inf')
    def minDiffInBST(self, root: TreeNode) -> int:
        if root.left != None:
            self.minDiffInBST(root.left)
        self.res = min(self.res, abs(root.val - self.pre))
        self.pre = root.val
        if root.right != None:
            self.minDiffInBST(root.right)
        return self.res
