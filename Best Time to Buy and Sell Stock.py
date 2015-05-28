# Say you have an array for which the ith element is the price of a given stock on day i.
#
# If you were only permitted to complete at most one transaction (ie, buy one and sell one share of the stock), design an algorithm to find the maximum profit.



class Solution:
    # @param {integer[]} prices
    # @return {integer}
    def maxProfit0(self, prices):
        """
        DP
        """
        if len(prices) <= 1:
            return 0

        minPrice = prices[0]
        maxProfit = 0

        for x in prices:
            minPrice = min(minPrice, x)
            maxProfit = max(maxProfit, x - minPrice)

        return maxProfit


    def maxProfit1(self, prices):
        """
        Greedy
        """
        maxProfit = 0
        for i in xrange(1, len(prices)):
            if prices[i] > prices[i-1]:
                maxProfit += prices[i] - prices[i-1]

        return maxProfit


    def maxProfit2(self, prices):
        """
        only allow for 2 transaction
        """


    def maxProfit(self, k, prices):
        """
        allow for k transaction
        """


s = Solution()
print s.maxProfit([5, 6, 7, 2, 3, 10 ])
