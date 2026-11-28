class Solution:
    def minWindow(self, s: str, t: str) -> str:
        runc={}
        res=[-1,1]
        reslen=float('inf')
        countert=Counter(t)
        have=0
        need=len(countert)
        i=0
        for j in range(len(s)):
            runc[s[j]]=runc.get(s[j],0)+1
            if s[j] in countert and runc[s[j]]==countert[s[j]]:
                have+=1
                while have==need:
                    runc[s[i]]-=1
                    if j-i+1<reslen:
                        reslen=j-i+1
                        res=[i,j+1]
                    if s[i] in countert and runc[s[i]]<countert[s[i]]:
                        have-=1
                    i+=1
        return s[res[0]:res[1]] if reslen!=float('inf') else ""