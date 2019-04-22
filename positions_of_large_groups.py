# In a string S of lowercase letters, these letters form consecutive groups of the same character.
# For example, a string like S = "abbxxxxzyy" has the groups "a", "bb", "xxxx", "z" and "yy".
# Call a group large if it has 3 or more characters.  We would like the starting and ending positions of every large group.
# The final answer should be in lexicographic order.

class Solution:
    def largeGroupPositions(self, S: str) -> List[List[int]]:
        left = 0
        right = 0
        current = 'A'
        answer = []
        for i in range(len(S)):
            if current != S[i]:
                current = S[i]
                if right - left >= 2:
                    answer.append([left, right])
                left = i
            right = i
            
        if right - left >= 2:
                answer.append([left, right])
            
        return answer
