class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        longest=0
        seen=set(nums)
        for i in nums:
            if i-1 not in seen:
                count=1
                cur=i
                while cur+1 in seen:
                    count+=1
                    cur+=1
                longest=max(longest,count)
        return longest