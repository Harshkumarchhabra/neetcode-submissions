class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        l,r=0,len(matrix[0])
        top,btm=0,len(matrix)

        while l<r and top<btm:
            for i in range(l,r):
                res.append(matrix[top][i])
            top+=1
            for i in range(top,btm):
                res.append(matrix[i][r-1])
            r-=1
            if not (l<r and top<btm):
                break
            for i in range(r-1,l-1,-1):
                res.append(matrix[btm-1][i])
            btm-=1
            for i in range(btm-1,top-1,-1):
                res.append(matrix[i][l])
            l+=1
        return res