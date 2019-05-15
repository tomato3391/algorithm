# Given an unsorted array of integers, find the length of longest increasing subsequence.

# Note:
#There may be more than one LIS combination, it is only necessary for you to return the length.
#Your algorithm should run in O(n2) complexity.

#Follow up: Could you improve it to O(n log n) time complexity?

class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails = []
        for i in nums:
            length = len(tails)
            replaced = False
            for idx in range(length):
                if i <= tails[idx]:
                    tails[idx] = i
                    replaced = True
                    break
            if not(replaced):
                tails.append(i)
                    
        return len(tails)
