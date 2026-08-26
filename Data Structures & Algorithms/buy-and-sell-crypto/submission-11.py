class Solution:
    def maxProfit(self, nums: List[int]) -> int:
        max_profit=0
        i=0
        for j in range(i+1,len(nums)):
            profit=nums[j]-nums[i]
            max_profit=max(max_profit,profit)
            if profit<0:
                i=j
        return max_profit