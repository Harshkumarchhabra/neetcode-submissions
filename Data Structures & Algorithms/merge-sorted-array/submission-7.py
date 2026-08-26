class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # 1st attempt 
        # nums1.sort()
        # for i in range(len(nums1)):
        #     if nums1[i]==0:
        #         nums1[i]=nums2[i]
        #     # nums1.append(nums2[i])
        # # nums1.sort()

        # 2nd attempt 
        # while m<len(nums1):
        #     j=0
        #     while j<n:
        #         nums1[m]=nums2[j]
        #         m+=1
        #         j+=1
        # nums1.sort()

        # 3rd attempt 
        while m>0 and n>0:
                p1=nums1[m-1]
                p2=nums2[n-1]
                if p1>p2:
                    nums1[m+n-1]=p1
                    m-=1
                else:
                    nums1[m+n-1]=p2
                    n-=1
        while n>0:
            nums1[m+n-1]=nums2[n-1]
            n-=1
            
        