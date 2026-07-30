class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        max_sum=float('-inf')
        summ=0
        # if len(nums)==1:
        #     return nums[0]
        for i in nums:
            if i>summ+i:
                summ=i
            else:
                summ+=i
            max_sum=max(max_sum,summ)
        return max_sum
