class Solution:
    def carFleet(self, target: int, position: List[int], speed: List[int]) -> int:
        
        new_arr=sorted(zip(position, speed),reverse=True)
        d, s = map(list, zip(*new_arr))
        stack=[]
        count=len(position)
        for i,j in zip(d,s):
            t=(target-i)/j
            if stack and t<=stack[-1]:
                count-=1
            else:
                stack.append(t)
        return count