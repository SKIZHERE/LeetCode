# 20. Valid Parentheses

class Solution(object):
    def isValid(self, s):
        """
        :type s: str
        :rtype: bool
        """
        d = {")":"(","}":"{","]":"["}
        if len(s)%2 != 0:
            return False
        es = []
        for i in s:
            if i in d.values():
                es.append(i)
            elif i in d:
                if not es or es.pop() != d[i]:
                    return False
        return not es