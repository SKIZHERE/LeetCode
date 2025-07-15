# 190. Reverse Bits

class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        n= format(n, '032b')
        op = 0
        for i in range(32):
            op = op + int(n[i])*(2**i)
        return op

