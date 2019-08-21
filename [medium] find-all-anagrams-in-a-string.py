# Given a string s and a non-empty string p, find all the start indices of p's anagrams in s.

# Strings consists of lowercase English letters only and the length of both strings s and p will not be larger than 20,100.

# The order of output does not matter.

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        ans = []
        s_table = dict()
        p_table = dict()
        s_length = len(s)
        p_length = len(p)
        
        for ch in p:
            p_table[ch] = p_table.get(ch, 0) + 1
        
        for i in range(s_length - p_length + 1):
            if i == 0:
                for ch in s[:p_length]:
                    s_table[ch] = s_table.get(ch, 0) + 1
            else:
                new_ch = s[i + p_length - 1]
                if s_table[s[i - 1]] == 1:
                    s_table.pop(s[i - 1])
                else:
                    s_table[s[i - 1]] -= 1
                s_table[new_ch] = s_table.get(new_ch, 0) + 1
            
            if p_table == s_table:
                ans.append(i)
            
        return ans
