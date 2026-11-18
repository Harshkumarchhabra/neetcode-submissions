class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        res=[0]*len(temperatures)
        for i,j in enumerate(temperatures):
            while stack and stack[-1][1]<j:
                stackI,stackT=stack.pop()
                res[stackI]=i-stackI
            stack.append((i,j))
        return res