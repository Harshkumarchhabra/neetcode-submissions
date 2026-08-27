class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        count=Counter(nums)
        # for i in nums:
        #     if i not in seen:
        # return count[]
        for i in nums:
            if count[i]==1:
                return i