class Solution:
    def floodFill(self, image: list[list[int]], sr: int, sc: int, color: int) -> list[list[int]]:
        m = len(image)
        n = len(image[0])
        ori = image[sr][sc]
        def dfs(i,j):
            dirs = [(-1,0),(1,0),(0,-1),(0,1)]
            if image[i][j] != ori:
                return
            image[i][j] = color
            for di,dj in dirs:
                ni = i + di
                nj = j + dj
                if 0<= ni < m and 0 <= nj < n:
                    dfs(ni,nj)
        
        if ori == color:
            return image
        
        dfs(sr,sc)
        return image