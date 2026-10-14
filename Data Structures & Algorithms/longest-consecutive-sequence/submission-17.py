class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count=0
        s=set(nums)
        for i in nums:
            count=1
            k=i
            if k-1 not in s:
                while k+1 in s:
                    count+=1
                    k+=1
            max_count=max(max_count,count)
        return max_count