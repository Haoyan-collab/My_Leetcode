from collections import deque
class Solution:
    def numIslands(self, grid: List[List[str]]) -> int:
        m = len(grid)
        n = len(grid[0])
        q = deque()
        ans = 0
        for i in range(m):
            for j in range(n):
                cur = grid[i][j]
                if cur == '1':
                    ans += 1
                    q.append((i,j))
                    grid[i][j] = '0'
                    while q:
                        x, y = q.popleft()
                        for (a,b) in [(x+1,y),(x-1,y),(x,y+1),(x,y-1)]:
                            if 0 <= a < m and 0 <= b < n and grid[a][b] == '1':
                                grid[a][b] = '0'
                                q.append((a,b))
        return ans