class Solution(object):
    def climbStairs(self, n):
        """
        :type n: int
        :rtype: int
        1,1,2,3,5,8,13
        """
        a = 1
        b = 1
        if n == 1:
            return n
        for i in range(1,n):
            x = a+b
            a = b
            b = x
        return x
