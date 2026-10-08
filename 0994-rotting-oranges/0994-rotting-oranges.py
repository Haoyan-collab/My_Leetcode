from collections import deque
class Solution:
    def orangesRotting(self, grid: list[list[int]]) -> int:
        m = len(grid)
        n = len(grid[0])

        q = deque()
        t = 0       #steps
        cnt = 0     #fresh orange
        for i in range(m):
            for j in range(n):
                if grid[i][j] == 2:
                    q.append((i,j,0))
                if grid[i][j] == 1:
                    cnt += 1
        if cnt == 0:
            return 0
        while q:
            i, j, t = q.popleft()
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            for x, y in dirs:
                ni = i + x
                nj = j + y
                if 0 <= ni < m and 0 <= nj < n and grid[ni][nj] == 1:
                    print("t:",t,"grid:",grid)
                    grid[ni][nj] = 2
                    q.append((ni,nj,t+1))
                    cnt -= 1
            if cnt == 0:
                return t + 1
        return -1