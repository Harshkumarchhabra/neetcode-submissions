class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        freq=Counter(nums)
        max_count=float('-inf')
        maj=0
        for n,count in freq.items():
            if count>max_count:
                max_count=count
                maj=n
        return maj