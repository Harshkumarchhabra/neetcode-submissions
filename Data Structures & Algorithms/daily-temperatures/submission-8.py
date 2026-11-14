class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        res=[0]*len(temperatures)
        stack=[]#pair:index and temperatures
        for i,j in enumerate(temperatures):
            while stack and j>stack[-1][1]:
                stackI,stackT=stack.pop()
                res[stackI]=i-stackI
            stack.append((i,j))
        return res