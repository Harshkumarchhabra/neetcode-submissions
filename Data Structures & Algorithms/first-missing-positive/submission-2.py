class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
        #Not solved in O(1) Auxilarry Space
        res=0
        Set=set(nums)
        for i in range(1,len(nums)+2):
            if i not in Set:
                res=i
                break
        return res
    
    

      # res=1
       # nums.sort()
       # for i in range(len(nums)):
      #      if nums[i]==res:
       #         res+=1
      #  return res