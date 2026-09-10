class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cs1=Counter(s1)
        count=len(s1)
        i=0
        for j in range(len(s2)-count+1):
            cs2=Counter(s2[i:i+count])
            if cs1==cs2:
                return True
            i+=1
        return False