class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        res=[]
        def dfs(i):
            if i>=len(nums):#base case
                res.append(nums.copy())#copy because nums changes everythimw we swap
                return res
            for j in range(i,len(nums)):
                nums[i],nums[j]=nums[j],nums[i]#swapping
                dfs(i+1)#moign forward
                nums[i],nums[j]=nums[j],nums[i]#backtracking (making the numers as they were before)
        dfs(0)
        return res