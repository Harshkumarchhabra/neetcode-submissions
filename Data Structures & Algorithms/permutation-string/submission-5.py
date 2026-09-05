class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        seen=Counter(s1)
        for i in range(len(s2)):
            count=0
            jump=0
            if s2[i] in seen:
                jump=i+len(s1)
                seen2=Counter(s2[i:jump])
                if seen==seen2:
                    return True
            # if count==len(s1):
            #         return True
        return False