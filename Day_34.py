# 202. Happy Number

class Solution(object):
    def isHappy(self, n):
        """
        :type n: int
        :rtype: bool
        """
        stack = []
        while n>1:
            if n in stack:
                return False
            stack.append(n)
            nstr = str(n)
            x = 0
            for i in nstr:
                x += int(i)**2
            n = x
        return True