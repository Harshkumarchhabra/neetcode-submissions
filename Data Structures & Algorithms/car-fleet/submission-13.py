class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=sorted(zip(position,speed),reverse=True)
        stack=[]
        res=len(position)
        for p,s in fleet:
            t=(target-p)/s
            if stack and stack[-1]>=t:
                res-=1
            else:
                stack.append(t)
        return res