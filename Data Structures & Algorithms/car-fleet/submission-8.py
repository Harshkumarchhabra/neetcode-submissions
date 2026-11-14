class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=sorted([[i,j] for i,j in zip(position,speed)],reverse=True)
        #or
        #fleet=list(zip(position,speed))
        res=len(position)
        stack=[]
        i=0
        for i,j in fleet:
            t=(target-i)/j
            if stack and stack[-1]>=t:
                res-=1
            else:
                stack.append(t)
        return res