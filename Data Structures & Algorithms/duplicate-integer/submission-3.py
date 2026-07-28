class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        for i in range(len(nums)):
            for j in range(i+1,len(nums)):
                if nums[i]==nums[j]:
                    return True
        return False
        # hashSet=set()
        # for i in nums:
        #     if i in hashSet:
        #         return True
        #     hashSet.add(i)
        # return False
         