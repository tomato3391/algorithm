# Given a matrix consisting of 0s and 1s, we may choose any number of columns in the matrix and flip every cell in that column.  Flipping a cell changes the value of that cell from 0 to 1 or from 1 to 0.

# Return the maximum number of rows that have all values equal after some number of flips.

# Note:

# 1 <= matrix.length <= 300
# 1 <= matrix[i].length <= 300
# All matrix[i].length's are equal
# matrix[i][j] is 0 or 1

class Solution:
    def maxEqualRowsAfterFlips(self, matrix: List[List[int]]) -> int:
        temp = matrix
        answer = 0
        while len(temp) > 1:
            first = temp[0]
            inv = list(map(lambda x: 1 if x == 0 else 0, first))
            cnt = temp.count(first) + temp.count(inv)
            
            if cnt > answer:
                answer = cnt
            
            temp = [x for x in temp if x != first and x != inv]
        
        return answer
