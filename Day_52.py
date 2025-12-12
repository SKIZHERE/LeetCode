# 338. Counting Bits

class Solution(object):
    def countBits(self, n):
        """
        :type n: int
        :rtype: List[int]
        """
        l = []
        for i in range(n+1):
            bitCount = 0
            while i !=0:
                bitCount += (i%2 != 0)
                i = i//2
            l.append(bitCount)
        return l

