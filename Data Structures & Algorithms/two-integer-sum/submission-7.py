class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        dic={}#value->index
        res=[]
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in dic:
                res.append(dic[diff])
                res.append(i)
                break
            dic[nums[i]]=i
        return res