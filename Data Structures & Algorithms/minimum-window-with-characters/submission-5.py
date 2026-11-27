class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res=[-1,1]
        reslen=float('inf')
        have=0
        countert=Counter(t)
        need=len(countert)
        i=0
        windc={}
        for j in range(len(s)):
            windc[s[j]]=windc.get(s[j],0)+1
            if s[j] in countert and windc[s[j]]==countert[s[j]]:
                have+=1
                while have==need:
                    if j-i+1<reslen:
                        reslen=j-i+1
                        res=[i,j+1]
                    windc[s[i]]-=1
                    if s[i] in countert and windc[s[i]]<countert[s[i]]:
                        have-=1
                    i+=1
        return s[res[0]:res[1]] if reslen!=float('inf') else ""