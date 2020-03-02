# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/

class Solution(object):
    def maxProfit(self, prices):

        if len(prices) == 0:
            return 0
        max_profit = 0
        min_price = prices[0]

        for i in range(1, len(prices)):
            min_price = min(min_price, prices[i])
            max_profit = max(max_profit, (prices[i] - min_price))
        return max_profit