# You have an array of logs.  Each log is a space delimited string of words.

# For each log, the first word in each log is an alphanumeric identifier.  Then, either:

# Each word after the identifier will consist only of lowercase letters, or;
# Each word after the identifier will consist only of digits.
# We will call these two varieties of logs letter-logs and digit-logs.  It is guaranteed that each log has at least one word after its identifier.

# Reorder the logs so that all of the letter-logs come before any digit-log.  The letter-logs are ordered lexicographically ignoring identifier, with the identifier used in case of ties.  The digit-logs should be put in their original order.

# Return the final order of the logs.

class Solution:
    def reorderLogFiles(self, logs: List[str]) -> List[str]:
        num = '0123456789'
        output = []
        digits = []
        struct = dict()
        for string in logs:
            lid, lstring = string.split(' ', maxsplit=1)
            if lstring[0] in num:
                digits.append(string)
            else:
                if struct.get(lstring) == None:
                    struct[lstring] = [lid]
                else:
                    struct[lstring].append(lid)
        
        for lstring in sorted(set(struct.keys())):
            for lid in sorted(set(struct[lstring])):
                output.append(lid + ' ' + lstring)
        
        return output + digits
        
