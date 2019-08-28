# You have an initial power P, an initial score of 0 points, and a bag of tokens.

# Each token can be used at most once, has a value token[i], and has potentially two ways to use it.

# If we have at least token[i] power, we may play the token face up, losing token[i] power, and gaining 1 point.
# If we have at least 1 point, we may play the token face down, gaining token[i] power, and losing 1 point.
# Return the largest number of points we can have after playing any number of tokens.

# Note:

# tokens.length <= 1000
# 0 <= tokens[i] < 10000
# 0 <= P < 10000

class Solution:
    def bagOfTokensScore(self, tokens: List[int], P: int) -> int:
        S = 0
        tokens.sort()
        
        while True:
            while len(tokens) > 0 and P >= tokens[0]:
                P -= tokens[0]
                S += 1
                tokens.pop(0)
            
            if len(tokens) > 1 and S > 0:
                P += tokens.pop()
                S -= 1
            else:
                return S
            
        return S + (len(tokens) if P >= sum(tokens) else 0)
