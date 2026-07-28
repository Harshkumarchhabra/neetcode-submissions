class Solution:
    def combinationSum(self, nums: List[int], target: int) -> List[List[int]]:
        
        # Input: 
        # nums = [3,4,5]  target = 16
        # Output: [[3,3,3,3,4],[3,3,5,5],[4,4,4,4],[3,4,4,5]]

        res=[]
        
        def dfg(i,cur,total):
            if total==target:
                res.append(cur.copy())
                return
            if i >= len(nums) or total > target:
                return
            #choosing
            cur.append(nums[i])
            dfg(i,cur,total+nums[i])

            #not choosing 
            cur.pop()
            dfg(i+1,cur,total)
        dfg(0,[],0)
        return res

