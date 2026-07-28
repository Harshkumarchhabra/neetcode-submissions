class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        Set=set(nums)
        max_count=0
        for i in nums:
            count=1
            while i+1 in Set:
                count+=1
                i+=1
            max_count=max(max_count,count)
        return max_count