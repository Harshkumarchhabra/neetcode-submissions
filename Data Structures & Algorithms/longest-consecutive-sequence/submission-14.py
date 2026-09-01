class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        max_count =0 
        seen=set(nums)
        for i in nums:
            if i-1 not in seen:
                count=1
                j=i
                while j+count in seen:
                    count+=1
                    # j+=1
                max_count=max(max_count,count)
        return max_count