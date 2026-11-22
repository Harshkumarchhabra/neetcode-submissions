class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        # we will keep the running sum in dictionary and we strat from 0 = 1
        dictionary={0:1} 
        res,count=0,0
        for i in nums:
            count+=i
            if count-k in dictionary:
                res+=dictionary[count-k]
            dictionary[count]=dictionary.get(count,0)+1
        return res