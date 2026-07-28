class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        ROW,COL=len(grid), len(grid[0])
        island=0
        def dfs(r,c):
            #base case
            if (r<0 or c<0 or r>=ROW or c>=COL or grid[r][c]=='0'):
                return
            #marking the starting point:
            grid[r][c]='0'
            dfs(r+1,c)
            dfs(r-1,c)
            dfs(r,c+1)
            dfs(r,c-1)

        for i in range(ROW):
            for j in range(COL):
                if grid[i][j]=='1':
                    island+=1
                    dfs(i,j)
            
        return island