class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        countS,countT=Counter(s),Counter(t)
        for i in countS:
            if countS[i]!=countT[i]:
                return False
        return True

