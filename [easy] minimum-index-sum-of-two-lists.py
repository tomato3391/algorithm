# Suppose Andy and Doris want to choose a restaurant for dinner, and they both have a list of favorite restaurants represented by strings.

# You need to help them find out their common interest with the least list index sum. If there is a choice tie between answers, output all of them with no order requirement. You could assume there always exists an answer.

# Note:
# The length of both lists will be in the range of [1, 1000].
# The length of strings in both lists will be in the range of [1, 30].
# The index is starting from 0 to the list length minus 1.
# No duplicates in both lists.

class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        answer = []
        idx = len(list1) + len(list2) - 2
        i = 0
        
        while idx >= i and i < len(list1):
            cur = list1[i]
            
            try:
                index = i + list2.index(cur, 0, idx - i + 1)
                
                if idx > index:
                    idx = index
                    answer.clear()
                    answer.append(cur)
                elif idx == index:
                    answer.append(cur)
                    
            except ValueError:
                continue
                
            finally:
                i += 1
        
        return answer
