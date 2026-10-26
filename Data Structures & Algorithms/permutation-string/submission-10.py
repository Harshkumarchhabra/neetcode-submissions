class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        count_s=Counter(s1)
        count=len(s1)
        for i in range(len(s2)-count+1):
            count_s2=Counter(s2[i:i+count])
            if count_s2==count_s:
                return True
            i+=1
        return False