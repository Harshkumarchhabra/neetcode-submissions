class Solution:
    def partitionLabels(self, s: str) -> List[int]:
        lastIndx={}
        for i,j in enumerate(s):
            lastIndx[j]=i

        res=[]
        size=end=0

        for i,j in enumerate(s):
            size+=1
            end=max(end,lastIndx[j])

            if i==end:
                res.append(size)
                size=0
        return res