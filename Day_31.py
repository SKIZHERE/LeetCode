# 191. Number of 1 Bits

class Solution(object):
    def hammingWeight(self, n):
        """
        :type n: int
        :rtype: int
        """
        n_new = str(bin(n)[2:])
        c = 0
        for i in n_new:
            if i == "1":
                c+=1
        return c
