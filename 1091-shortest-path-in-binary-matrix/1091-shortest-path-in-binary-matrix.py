from collections import deque
class Solution:
    def shortestPathBinaryMatrix(self, grid: list[list[int]]) -> int:
        n = len(grid)
        dirs = [(0,1),(0,-1),(1,1),(1,-1),(1,0),(-1,0),(-1,1),(-1,-1)]
        if grid[0][0]==1 or grid[n-1][n-1]==1:
            return -1
        ans = -1
        q = deque()
        q.append((0,0,0))
        steps = 0
        while q:
            i,j,steps = q.popleft()
            if i==n-1 and j==n-1:
                ans = steps
                break
            for x,y in dirs:
                ni = i+x
                nj = j+y
                if 0<=ni<n and 0<=nj<n and grid[ni][nj]==0:
                    q.append((ni,nj,steps+1))
                    grid[ni][nj] = 1
        return ans+1 if ans > -1 else -1