# 67. Add Binary

class Solution(object):
    def addBinary(self, a, b):
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        x,y,fa = 0,0,""
        for i in range(len(a)):
            x = x + int(a[i])*(2**(len(a) -1 - i))
        for i in range(len(b)):
            y = y + int(b[i])*(2**(len(b) -1 - i))
        z = x+y
        while z>=1:
            if z == 1:
                return "1" + fa
            a = z%2
            z = z//2
            fa = str(a) + fa
        return "0"
