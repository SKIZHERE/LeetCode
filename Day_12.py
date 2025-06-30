# 66. Plus One

class Solution(object):
    def plusOne(self, digits):
        """
        :type digits: List[int]
        :rtype: List[int]
        """
        x = 0
        for i,obj in enumerate(reversed(digits)):
            x = x+obj*(10**i)
        x = str(x+1)
        newDigits = [int(y) for y in x]
        return newDigits
