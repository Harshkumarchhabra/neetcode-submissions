class Solution:
    def rob(self, nums: List[int]) -> int:
        n=len(nums)
        mem=[-1]*n
        def dfs(i):
            if i>=n:
                return 0
            if mem[i]!= -1:
                return mem[i]
            mem[i]=max(dfs(i+1), nums[i]+dfs(i+2))
            return mem[i]
        return dfs(0)
        