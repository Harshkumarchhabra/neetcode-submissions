class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        subset=[]

        def dfs(i):
            if i>=len(nums):
                res.append(subset.copy())
                return
            #adding/choosing the number
            subset.append(nums[i])
            dfs(i+1)

            #not choosing the number
            subset.pop()
            dfs(i+1)
        dfs(0)
        return res

        
# Input: nums = [1,2,3]
#Output: [[],[1],[2],[1,2],[3],[1,3],[2,3],[1,2,3]]

