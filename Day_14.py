# 69. Sqrt(x)

class Solution(object):
    def mySqrt(self, x):
        """
        :type x: int
        :rtype: int
        *Do not use x**0.5*
        """
        if x == 0:
            return 0
        y = x
        while y*y>x:
            y = (y+x//y)//2
        return y