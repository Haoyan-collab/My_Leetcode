class Solution:
    def solve(self, board: list[list[str]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        visited = {}
        m = len(board)
        n = len(board[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1)]

        def dfs(i,j):
            if (i,j) in visited:
                return
            visited[(i,j)] = 1
            for x,y in dirs:
                ni = x+i
                nj = y+j
                if 0<=ni<m and 0<=nj<n:
                    if board[ni][nj] == 'O':
                        board[ni][nj] = 'T'
                        dfs(ni,nj)
            return
        
        for i in range(m):
            if board[i][0] == 'O':
                board[i][0] = 'T'
                dfs(i,0)
            if board[i][n-1] == 'O':
                board[i][n-1] = 'T'
                dfs(i,n-1)
        
        for j in range(1,n-1):
            if board[0][j] == 'O':
                board[0][j] = 'T'
                dfs(0,j)
            if board[m-1][j] == 'O':
                board[m-1][j] = 'T'
                dfs(m-1,j)
            
        for i in range(m):
            for j in range(n):
                if board[i][j] == 'T':
                    board[i][j] = 'O'
                elif board[i][j] == 'O':
                    board[i][j] = 'X'

                
