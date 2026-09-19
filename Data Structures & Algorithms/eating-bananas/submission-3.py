class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=99999999999
        while l<=r:
            mid=(l+r)//2

            count=0
            for i in piles:
                if mid>=i:
                    count+=1
                elif i%mid==0:
                    e=i//mid
                    count+=e
                else:
                    e=(i//mid)+1
                    count+=e
            if count>h:
                l=mid+1
            elif count<=h:
                res=mid
                r=mid-1
            # res=min(res,count)
        return res
