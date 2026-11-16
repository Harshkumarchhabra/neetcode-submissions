class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=sorted(zip(position,speed),reverse=True)
        res=len(position)
        stack=[]
        for p,s in fleet:
            t=(target-p)/s
            if stack and t<=stack[-1]:
                res-=1
            else:
                stack.append(t)
        return res