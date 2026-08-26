class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        # nums1.sort()
        # for i in range(len(nums1)):
        #     if nums1[i]==0:
        #         nums1[i]=nums2[i]
        #     # nums1.append(nums2[i])
        # # nums1.sort()
        i=0
        while m<len(nums1):
            j=0
            while j<n:
                nums1[m]=nums2[j]
                m+=1
                j+=1
        nums1.sort()