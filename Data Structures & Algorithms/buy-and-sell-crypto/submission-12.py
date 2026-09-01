class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        max_profit=0
        j=0
        for i in range(j+1,len(prices)):
            profit = prices[i]-prices[j]
            max_profit=max(max_profit,profit)
            if prices[i]<prices[j]:
                j=i
        return max_profit