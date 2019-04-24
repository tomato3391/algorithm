# Given a word, you need to judge whether the usage of capitals in it is right or not.

# We define the usage of capitals in a word to be right when one of the following cases holds:

# All letters in this word are capitals, like "USA".
# All letters in this word are not capitals, like "leetcode".
# Only the first letter in this word is capital if it has more than one letter, like "Google".
# Otherwise, we define that this word doesn't use capitals in a right way.

class Solution:
    def detectCapitalUse(self, word: str) -> bool:
        length = len(word)
        if length == 1:
            return True
        if word[0] < 'a' and word[1] < 'a':
            for i in range(1, length):
                if word[i] > 'Z':
                    return False
        else:
            for i in range(1, length):
                if word[i] < 'a':
                    return False
        return True
