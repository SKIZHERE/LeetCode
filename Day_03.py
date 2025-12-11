# 13. Roman to Integer

class Solution(object):
    def romanToInt(self, s):
        f = 0

        d = {"M": 1000, "D": 500, "C": 100, "L": 50, "X": 10, "V": 5, "I": 1}
        for i in range(len(s)):
            if i < len(s) - 1 and d[s[i]] < d[s[i + 1]]:
                f = f - d[s[i]]
            else:
                f = f + d[s[i]]

        return f
