class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        maxProf=0
        i=0
        for j in range(i+1,len(prices)):
            p=0
            if prices[j]<prices[i]:
                i=j
            p=max(p,prices[j]-prices[i])
            maxProf=max(maxProf,p)
        return maxProf