class Solution:
    def makesquare(self, MS: List[int]) -> bool:
        length=sum(MS)//4
        sides=[0]*4

        if sum(MS)/4 != length:
            return False
        MS.sort(reverse=True)

        def backtrack(i):
            if i==len(MS):
                return True
            for j in range(4):
                if sides[j] + MS[i]<=length:
                    sides[j]+=MS[i]
                    if backtrack(i+1):
                        return True
                    sides[j]-=MS[i]
            return False
        return backtrack(0)