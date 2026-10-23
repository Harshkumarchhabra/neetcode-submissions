class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        fleet=sorted(zip(position,speed),reverse=True)
        time=[]
        count=len(position)
        for pos,sp in fleet:
            t=(target-pos)/sp
            if time and time[-1]>=t:
                count-=1
            else:
                time.append(t)
        return count