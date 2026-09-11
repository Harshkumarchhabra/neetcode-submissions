class Solution:
    def minWindow(self, s: str, t: str) -> str:
        res=""
        counter_t=Counter(t)
        # count=1
        i=0
        wind_count={}
        have=0
        need=len(counter_t)
        res=[-1,1]
        reslen=float('inf')
        for j in range(len(s)):
            wind_count[s[j]]=wind_count.get(s[j],0)+1
            if s[j] in counter_t and wind_count[s[j]]==counter_t[s[j]]:
                have+=1
                while have==need:
                    if j-i+1 <reslen:
                        reslen=j-i+1
                        res=[i,j]
                    wind_count[s[i]]-=1
                    if s[i] in counter_t and wind_count[s[i]]<counter_t[s[i]]:
                        have-=1
                    i+=1
        return s[res[0]:res[1]+1] if reslen!=float('inf') else ""