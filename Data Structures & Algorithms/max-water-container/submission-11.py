class Solution:
    def maxArea(self, heights: List[int]) -> int:
        l=0
        r=len(heights)-1
        water=0
        while l<=r:
            waterr=(r-l)*min(heights[l],heights[r])
            water=max(water,waterr)
            if heights[l]<=heights[r]:
                l+=1
            else:
                r-=1
        return water