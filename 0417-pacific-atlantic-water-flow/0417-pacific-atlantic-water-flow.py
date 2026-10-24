from collections import defaultdict
class Solution:
    def pacificAtlantic(self, heights: list[list[int]]) -> list[list[int]]:
        m = len(heights)
        n = len(heights[0])
        dirs = [(0,1),(0,-1),(1,0),(-1,0)]
        ans = []
        p = set()
        a = set()
        def dfs(r,c,path):
            if (r,c) in path:
                return
            path.add((r,c))
            for x,y in dirs:
                nr = x+r
                nc = y+c
                if 0<=nr<m and 0<=nc<n and heights[nr][nc] >= heights[r][c]:
                    dfs(nr,nc,path)
        for r in range(m):
            dfs(r,0,p)
            dfs(r,n-1,a)
        for c in range(n):
            dfs(0,c,p)
            dfs(m-1,c,a)
        ans = [[r,c] for r,c in p&a]
        return ans
        # def dfs_p(r,c,path):
        #     if (r,c) in path:
        #         return
        #     path[(r,c)] = True
        #     if r==0 or c==0:
        #         return True
        #     for x,y in dirs:
        #         nr = r+x
        #         nc = c+y
        #         if 0<=nr<m and 0<=nc<n and heights[nr][nc] <= heights[r][c] and dfs_p(nr,nc,path):
        #             return True
        #     return False

        # def dfs_a(r,c,path):
        #     if (r,c) in path:
        #         return
        #     path[(r,c)] = True
        #     print(m,n)
        #     if r==m-1 or c==n-1:
        #         return True
        #     for x,y in dirs:
        #         nr = r+x
        #         nc = c+y
        #         if 0<=nr<m and 0<=nc<n and heights[nr][nc] <= heights[r][c] and dfs_a(nr,nc,path):
        #             return True
        #     return False

        # for r in range(m):
        #     for c in range(n):
        #         paths = defaultdict(bool)
        #         patha = defaultdict(bool)
        #         if dfs_p(r,c,paths) and dfs_a(r,c,patha):
        #             ans.append([r,c])
                    
        # return ans