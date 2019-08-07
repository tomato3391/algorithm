# Given an array nums, write a function to move all 0's to the end of it while maintaining the relative order of the non-zero elements.

# Note:

# You must do this in-place without making a copy of the array.
# Minimize the total number of operations.

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        nums[:] = [n for n in nums if n != 0] + [0] * nums.count(0)
