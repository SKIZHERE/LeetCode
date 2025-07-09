#168. Excel Sheet Column Title

class Solution(object):
    def convertToTitle(self, columnNumber):
        """
        :type columnNumber: int
        :rtype: str
        """
        op = ""
        while columnNumber > 0:
            columnNumber -= 1
            charr = columnNumber % 26
            op = chr(65 + charr) + op
            columnNumber = columnNumber // 26
        return op
