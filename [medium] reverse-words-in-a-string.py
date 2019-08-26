# Given an input string, reverse the string word by word.

# Note:

# A word is defined as a sequence of non-space characters.
# Input string may contain leading or trailing spaces. However, your reversed string should not contain leading or trailing spaces.
# You need to reduce multiple spaces between two words to a single space in the reversed string.

class Solution:
    def reverseWords(self, s: str) -> str:
        rev = [word for word in s.split(' ') if word != '']
        rev.reverse()
        return ' '.join(rev)
