# 367. Valid Perfect Square

class Solution(object):
    def isPerfectSquare(self, num):
        """
        :type num: int
        :rtype: bool
        """
        a = num ** 0.5
        return int(a) == a