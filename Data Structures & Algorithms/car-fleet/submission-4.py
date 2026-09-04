class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        # 1,4 -> 4,6 -> 7,8 -> 10,10 = 1 car fleet
        # 4,1,0,7 -> 6,3,1,8 -> 8,5,2,9 -> 10,7,3,10 -> 10,9,4,10 = 3 car fleet
        # 0,1,2,3,4,5,6,7,8,9
        fleet =sorted(zip(position,speed),reverse = True)
        time=[]
        count=len(position)
        for p,s in fleet:
            t=(target-p)/s
            if time and time[-1]>=t:
                count-=1
            else:
                time.append(t)
        return count