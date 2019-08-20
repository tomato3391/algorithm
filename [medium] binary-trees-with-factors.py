# Given an array of unique integers, each integer is strictly greater than 1.

# We make a binary tree using these integers and each number may be used for any number of times.

# Each non-leaf node's value should be equal to the product of the values of it's children.

# How many binary trees can we make?  Return the answer modulo 10 ** 9 + 7.

# Note:

# 1 <= A.length <= 1000.
# 2 <= A[i] <= 10 ^ 9.

class Solution:
    def numFactoredBinaryTrees(self, A: List[int]) -> int:
        matches = dict()
        
        for num in sorted(A):
            matches[num] = sum([matches[div] * matches.get(num / div, 0) for div in matches.keys() if num % div == 0]) + 1
        
        return sum(matches.values()) % (10 ** 9 + 7)
