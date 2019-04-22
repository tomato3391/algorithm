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
