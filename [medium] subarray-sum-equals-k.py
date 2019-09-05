# Given an array of integers and an integer k, you need to find the total number of continuous subarrays whose sum equals to k.

# Note:
# The length of the array is in range [1, 20,000].
# The range of numbers in the array is [-1000, 1000] and the range of the integer k is [-1e7, 1e7].

class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        ans = 0
        cur = 0
        sums = {0: 1}
        
        for i in range(len(nums)):
            cur += nums[i]
            ans += sums.get(cur - k, 0)
            sums[cur] = sums.get(cur, 0) + 1
            print(sums)
            
        return ans
