# In English, we have a concept called root, which can be followed by some other words to form another longer word - let's call this word successor. For example, the root an, followed by other, which can form another word another.

# Now, given a dictionary consisting of many roots and a sentence. You need to replace all the successor in the sentence with the root forming it. If a successor has many roots can form it, replace it with the root with the shortest length.

# You need to output the sentence after the replacement.

# Note:

# The input will only have lower-case letters.
# 1 <= dict words number <= 1000
# 1 <= sentence words number <= 1000
# 1 <= root length <= 100
# 1 <= sentence words length <= 1000

class Solution:
    def replaceWords(self, dict: List[str], sentence: str) -> str:
        words = sentence.split(' ')
        
        for i in range(len(words)):
            for pre in dict:
                if words[i].startswith(pre):
                    words[i] = pre
        
        return ' '.join(words)
