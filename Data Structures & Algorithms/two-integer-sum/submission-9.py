class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        # given is array and a target 
        # i have to return indeces of 2 numbers such that 
        # their sum = target 
        #  if no numbers liek that we return empty array[]
        seen={}
        for i in range(len(nums)):
            diff=target-nums[i]
            if diff in seen:
                return [seen[diff],i]
            seen[nums[i]]=i
        return []