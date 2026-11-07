from collections import deque
class Solution:
    def shortestBridge(self, grid: list[list[int]]) -> int:
        n = len(grid)
        visited = {}
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]
        q = deque()
        def dfs(i,j):
            if (i,j) in visited:
                return
            visited[(i,j)] = 1
            q.append((i,j))
            for x,y in dirs:
                ni = x+i
                nj = y+j
                if 0<=ni<n and 0<=nj<n and grid[ni][nj]==1:
                    dfs(ni,nj)
        found = False
        for i in range(n):
            if found:
                break
            for j in range(n):
                if grid[i][j]==1:
                    dfs(i,j)
                    found = True
                    break
        steps = 0

        while q:
            for _ in range(len(q)):
                i,j = q.popleft()
                for x,y in dirs:
                    ni = x+i
                    nj = y+j
                    if 0<=ni<n and 0<=nj<n and (ni,nj) not in visited:
                        if grid[ni][nj]==1:
                            return steps
                        else:
                            grid[ni][nj]=1
                            visited[(ni,nj)]=1
                            q.append((ni,nj))
            steps += 1

        return steps
