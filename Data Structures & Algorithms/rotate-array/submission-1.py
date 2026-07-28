class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n=len(nums)
        k=k%n
        first=nums[:n-k] #numbers except last k elements
        second=nums[n-k:] #last k elements

        nums[:] =  second + first
