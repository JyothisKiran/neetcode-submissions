class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        n = len(prices)
        buy = prices[0]
        buyIndex=0
        profit = 0

        for i in range(n):
            if (buy > prices[i]):
                buy=prices[i]
                buyIndex=i
            if(i>buyIndex):
                profit  = max(prices[i]-buy, profit)
        return profit
