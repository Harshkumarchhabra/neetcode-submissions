class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        cur=0
        count=0
        check={0:1}#for edge cases 
        for i in nums:
            cur+=i
            if cur-k in check:
                count+=check[cur-k]
            check[cur]=check.get(cur,0)+1
        return count