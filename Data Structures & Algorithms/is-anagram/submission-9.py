class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS,countT=Counter(s),Counter(t)
        for i,v in countS.items():
            if countT[i]!=v:
                return False
        return True

