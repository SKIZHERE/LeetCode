# 121. Best Time to Buy and Sell Stock

#MySoln
"""
class Solution(object):
    def maxProfit(self, prices):
        """
        # :type prices: List[int]
        # :rtype: int
        """
        lp = []
        for i in range(len(prices)-1):
            for j in range(i+1,len(prices)-1):
                profit = prices[j] - prices[i]
                if  profit > 0 and j>i :
                    lp.append(profit)
        if lp == []:
            return 0
        return max(lp)
"""

#Took Help
class Solution(object):
    def maxProfit(self, prices):
        """
        :type prices: List[int]
        :rtype: int
        """
        minp = float('inf')
        maxp = 0
        for i in prices:
            maxp = max(maxp, i - minp)
            minp = min(minp, i)
        return maxp
