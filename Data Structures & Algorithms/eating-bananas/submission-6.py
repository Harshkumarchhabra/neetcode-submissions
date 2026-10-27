class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        l=1
        r=max(piles)
        res=max(piles)
        while l<=r:
            m=(l+r)//2
            count=0
            for n in piles:
                if n%m==0:
                    val=n/m
                    count+=val
                else:
                    val=n//m
                    count+=(val+1)
            if count>h:
                l=m+1
            elif count<=h:
                r=m-1
                res=min(res,m)
        return res