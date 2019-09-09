# Given an array of strings, group anagrams together.

# Note:

# All inputs will be in lowercase.
# The order of your output does not matter.

class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        ans = dict()
        
        for word in sorted(strs):
            key = tuple(sorted(word))
            ans[key] = ans.get(key, []) + [word]
        
        return ans.values()
