class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        profit = 0
        for i in range(n-1):
            d = prices[i+1] - prices[i]
            if d > 0:
                profit += d
        return profit