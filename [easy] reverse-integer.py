# Given a 32-bit signed integer, reverse digits of an integer.

# Note:
# Assume we are dealing with an environment which could only store integers within the 32-bit signed integer range: [−231,  231 − 1]. For the purpose of this problem, assume that your function returns 0 when the reversed integer overflows.

class Solution:
    def reverse(self, x: int) -> int:
        ans = int(str(x)[::-1]) if x >= 0 else int('-' + str(x)[:0:-1])
        return ans if ans >= -(2 ** 31) and ans <= 2 ** 31 - 1 else 0
