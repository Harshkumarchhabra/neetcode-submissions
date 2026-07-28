class Solution:
    def majorityElement(self, nums: List[int]) -> List[int]:
        Size=len(nums)//3
        mapping={}
        for i in nums:
            if i in mapping:
                mapping[i]+=1
            else:
                mapping[i]=1
        
        res=[]
        for num,count in mapping.items():
            if count > Size:
                res.append(num)
        
        return res