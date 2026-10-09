class Solution:
    def minWindow(self, s: str, t: str) -> str:
        #we add string and it freq in a map 
        # if count of window = countert have +=1
        #while have = need if currnt window is less then prev wemake the reslen to cur window
        # and add the winow in res 
        # we delte strinf and count of string at i and move i
        # if that is in window we red have
        res=[-1,1]
        wind_count={}
        countert=Counter(t)
        i=0
        have=0
        need=len(countert)
        reslen=float('inf')
        for j in range(len(s)):
            wind_count[s[j]]=wind_count.get(s[j],0)+1
            if s[j] in countert and wind_count[s[j]]==countert[s[j]]:
                have+=1
                while have==need:
                    if j-i+1<reslen:
                        reslen=j-i+1
                        res=[i,j]
                    wind_count[s[i]]-=1
                    if s[i] in countert and wind_count[s[i]]<countert[s[i]]:
                        have-=1
                    i+=1
        return s[res[0]:res[1]+1] if reslen!=float('inf') else ""