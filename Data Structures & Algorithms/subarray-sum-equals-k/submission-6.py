class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        sub={0:1}
        run,res=0,0

        for i in nums:
            run+=i
            if run-k in sub:
                res+=sub[run-k]
            sub[run]=sub.get(run,0)+1
        return res