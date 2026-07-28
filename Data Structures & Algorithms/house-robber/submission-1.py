class Solution:
    def rob(self, nums: List[int]) -> int:
        #top-down
        # n=len(nums)
        # mem=[-1]*n
        # def dfs(i):
        #     if i>=n:
        #         return 0
        #     if mem[i]!= -1:
        #         return mem[i]
        #     mem[i]=max(dfs(i+1), nums[i]+dfs(i+2))
        #     return mem[i]
        # return dfs(0)

        #optimized d-P
        
        rob1,rob2=0,0
        #[rob1,rob2,n,n+1,n+2,.......]
        for n in nums:
            temp=max(rob1+n,rob2)
            rob1=rob2
            rob2=temp
        return rob2
        