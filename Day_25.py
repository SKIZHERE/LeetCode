# 171. Excel Sheet Column Number

class Solution(object):
    def titleToNumber(self, columnTitle):
        """
        :type columnTitle: str
        :rtype: int
        """
        l,num = [],0
        for i in columnTitle:
            l = [i] + l
        for j in range(len(columnTitle)):
            num = num + (ord(l[j])-64)*(26**j)
        return num