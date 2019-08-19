# Given an array A of 0s and 1s, consider N_i: the i-th subarray from A[0] to A[i] interpreted as a binary number (from most-significant-bit to least-significant-bit.)

# Return a list of booleans answer, where answer[i] is true if and only if N_i is divisible by 5.

# Note:

# 1 <= A.length <= 30000
# A[i] is 0 or 1

class Solution:
    def prefixesDivBy5(self, A: List[int]) -> List[bool]:
        for i in range(len(A) - 1):
            A[i + 1] += A[i] * 2 % 5
            
        return [i % 5 == 0 for i in A]
