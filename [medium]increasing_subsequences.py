# Given an integer array, your task is to find all the different possible increasing subsequences of the given array, and the length of an increasing subsequence should be at least 2.

# Note:

# The length of the given array will not exceed 15.
# The range of integer in the given array is [-100,100].
# The given array may contain duplicates, and two equal integers should also be considered as a special case of increasing sequence.

class Solution:
    def findSubsequences(self, nums: List[int]) -> List[List[int]]:
        ans = {()}
        
        for num in nums:
            ans = ans | {tup + (num,) for tup in ans if not tup or tup[-1] <= num}
            
        return [tup for tup in ans if len(tup) >= 2]
