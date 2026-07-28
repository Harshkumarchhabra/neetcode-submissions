class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        # binary search way is difficult and still left , so do it first
        
        i,j=0,0
        n3=[]
        while i < len(nums1) and j < len(nums2):
            if nums1[i] < nums2[j]:
                n3.append(nums1[i])
                i+=1
            else:
                n3.append(nums2[j])
                j+=1
        while i < len(nums1):
            n3.append(nums1[i])
            i+=1
        while j < len(nums2):
            n3.append(nums2[j])
            j+=1

        n=len(n3)
        if n%2==0:
            ans=(n3[n//2-1]+n3[n//2])/2.0
        else:
            ans=float(n3[n//2])
        
        return ans
            
                

        