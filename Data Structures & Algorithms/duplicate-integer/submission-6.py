class Solution:
    def hasDuplicate(self, nums: List[int]) -> bool:
        Count=Counter(nums)
        for i,j in Count.items():
            if j>1:
                return True
        return False