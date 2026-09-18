class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        # mindif=99999999999999999
        l=0
        r=len(nums)-1
        if target>nums[r]:
            return r+1
        while l<=r:
            mid=(l+r)//2
            if nums[mid]<target:
                l+=1
                
            elif nums[mid]>target:
                r-=1
            else:
                return mid
            # dif=target-nums[mid]
            # if dif<0:
            #     dif=dif*-1
            # if mindif>dif:
            #     mindif=mid
        return mid