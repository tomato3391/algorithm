# Given a non-negative integer num represented as a string, remove k digits from the number so that the new number is the smallest possible.

# Note:
# The length of num is less than 10002 and will be ≥ k.
# The given num does not contain any leading zero.

class Solution:
    def removeKdigits(self, num: str, k: int) -> str:
        if len([ch for ch in num if ch != '0']) <= k:
            return '0'
        while k > 0:
            test, num = num[:k], num[k:]
            if num[0] != '0' and test.count('0') == 0:
                num = test + num
                break
            k = test.count('0')
            if k > 0:
                right = test.rindex('0')
                k += len(test) - right - 1
                num = test[right + 1:] + num
            while num.startswith('0'):
                num = num[1:]
        
        if k > 0:
            l = len(num) - k
            ans = ''
            
            for i in range(l, 0, -1):
                if i == len(num):
                    ans += num
                    break
                min_num = min(num[:len(num) - i + 1])
                ans += min_num
                num = num[num.index(min_num) + 1:]
            
            return ans
        else:
            return num
