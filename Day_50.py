# 290. Word Pattern

class Solution(object):
    def wordPattern(self, pattern, s):
        """
        :type pattern: str
        :type s: str
        :rtype: bool
        """
        d = {}
        s = s.split()
        if len(pattern) != len(s): return False
        for i in range(len(pattern)):
            if pattern[i] in d.keys():
                if d[pattern[i]] != s[i]:
                    return False
            else:
                d[pattern[i]] = s[i]
        if len(d.values()) == len(set(d.values())): return True
        else: return False