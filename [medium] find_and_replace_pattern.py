# You have a list of words and a pattern, and you want to know which words in words matches the pattern.
# A word matches the pattern if there exists a permutation of letters p so that after replacing every letter x in the pattern with p(x), we get the desired word.
# (Recall that a permutation of letters is a bijection from letters to letters: every letter maps to another letter, and no two letters map to the same letter.)
# Return a list of the words in words that match the given pattern. 
# You may return the answer in any order.

# Note:
# 1 <= words.length <= 50
# 1 <= pattern.length = words[i].length <= 20

class Solution:
    def findAndReplacePattern(self, words: List[str], pattern: str) -> List[str]:
        answer = []
        letters = 'abcdefghijklmnopqrstuvwxyz'
        idx = 45
        for i in range(len(pattern)):
            if pattern[i] not in letters:
                continue
            pattern = pattern.replace(pattern[i], chr(idx))
            idx += 1
        for word in words:
            idx = 45
            temp = word
            for i in range(len(temp)):
                if temp[i] not in letters:
                    continue
                temp = temp.replace(temp[i], chr(idx))
                idx += 1
            if temp == pattern:
                answer.append(word)
        
        return answer
