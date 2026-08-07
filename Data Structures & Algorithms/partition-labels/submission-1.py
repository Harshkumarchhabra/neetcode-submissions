class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        counter=Counter(s)
        unresolved=set()
        count=0
        lis=[]
        for i in s:
            if i not in unresolved:
                unresolved.add(i)
                counter[i]-=1
                count+=1
            else:
                counter[i]-=1
                count+=1
            if counter[i]==0:
                unresolved.remove(i)
            if len(unresolved)==0:
                lis.append(count)
                count=0
        return lis