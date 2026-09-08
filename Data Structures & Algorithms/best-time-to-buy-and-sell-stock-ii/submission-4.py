class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        total=0
        for j in range(1,len(prices)):
            if prices[j]>prices[j-1]:
                total+=prices[j]-prices[j-1]
        return total