class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        lefty=[1]*len(nums)
        righty=[1]*len(nums)
        res=[1]*len(nums)

        l=nums[-1]
        for i in range(len(nums)-2,-1,-1):
            lefty[i]=l
            l=l*nums[i]

        r=nums[0]
        for i in range(1,len(nums)):
            righty[i]=r
            r=r*nums[i]
        
        for i in range(len(nums)):
            res[i]=lefty[i]*righty[i]
        return res
# [1,1,2,8]
# [48,24,6,1]