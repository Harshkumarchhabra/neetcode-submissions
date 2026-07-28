class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        # nums.sort()
        Set=set(nums)
        Long=0
        for i in nums:
            if i-1 not in Set:
                leng=1
                while i+leng in Set:
                    leng+=1
                Long=max(Long,leng)
        return Long
        