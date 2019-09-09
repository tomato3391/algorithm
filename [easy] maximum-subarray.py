# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        sub = _max = 0
        
        for num in nums:
            sub += num
            if sub <= 0:
                sub = 0
            else:
                if _max < sub:
                    _max = sub
                
        return _max if _max > 0 else max(nums)
