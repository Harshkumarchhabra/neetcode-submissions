class Solution:
    def trap(self, height: List[int]) -> int:
        l=0
        r=len(height)-1
        max_l=0
        max_r=0
        max_a=0
        while l<=r:
            max_l=max(max_l,height[l])
            max_r=max(max_r,height[r])
            if max_l<=max_r:
                max_a+=(max_l-height[l])
                l+=1
            else:
                max_a+=(max_r-height[r])
                r-=1
        return max_a