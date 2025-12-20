# 374. Guess Number Higher or Lower

# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num):

class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        l = 1
        while l!=n:
            res = guess((l+n)//2)
            if res>0:
                l = (l+n)//2 + 1
                continue
            elif res<0:
                n = (l+n)//2 - 1
                continue
            break
        return (l+n)//2