class Solution:
    def climbStairs(self, n: int) -> int:
        # recursion
        # if n<=1:
        #     return 1

        # return self.climbStairs(n-1)+self.climbStairs(n-2)

        # memoization / 1-d D-P / top - down D-P

        cache=[-1]*n
        def mem(i):
            if i>=n:
                return i==n
            if cache[i]!= -1:
                return cache[i]
            cache[i]=mem(i+1) + mem(i+2)
            return cache[i]
        return mem(0)
    
    
        