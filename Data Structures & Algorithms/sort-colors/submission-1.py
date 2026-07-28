class Solution:
    def sortColors(self, nums: List[int]) -> None:
        #nums.sort()
        l,r=0,len(nums)-1
        i=0

        def swap(l,r):
            temp=nums[l]
            nums[l]=nums[r]
            nums[r]=temp
        
        while i<=r:
            if nums[i]==0:
                swap(l,i)
                l+=1
            elif nums[i]==2:
                swap(r,i)
                r-=1
                i-=1# it wll cause errors in places where we have 1's in starting like in ex [1,2,0] dry run this and you will understand
            i+=1
