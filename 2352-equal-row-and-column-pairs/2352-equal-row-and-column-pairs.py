class Solution:
    def equalPairs(self, grid: list[list[int]]) -> int:
        ccnt = defaultdict(int)
        m = len(grid)
        n = len(grid[0])
        ans = 0


        for j in range(n):
            ccnt[tuple(grid[i][j] for i in range(m))] += 1

        for row in grid:
            if tuple(row) in ccnt:
                ans += ccnt[tuple(row)]

        return ans