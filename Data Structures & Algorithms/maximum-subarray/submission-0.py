class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        cur=0
        maxsum=nums[0]
        for i in nums:
            cur=max(cur,0)
            cur+=i
            maxsum=max(maxsum,cur)
        return maxsum