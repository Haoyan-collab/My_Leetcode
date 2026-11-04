from collections import deque
class Solution:
    def updateMatrix(self, mat: list[list[int]]) -> list[list[int]]:
        steps = 1
        m = len(mat)
        n = len(mat[0])
        q = deque()
        dirs = [(-1,0),(1,0),(0,1),(0,-1)]
        for i in range(m):
            for j in range(n):
                if mat[i][j]==0:
                    q.append((i,j))
                else:
                    mat[i][j] = -1
        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for x,y in dirs:
                    ni = x+i
                    nj = y+j
                    if 0<=ni<m and 0<=nj<n and mat[ni][nj]==-1:
                        mat[ni][nj] = steps
                        q.append((ni,nj))

            steps += 1
        
        return mat