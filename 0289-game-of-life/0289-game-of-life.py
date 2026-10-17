class Solution:
    def gameOfLife(self, board: list[list[int]]) -> None:
        """
        Do not return anything, modify board in-place instead.
        """
        m = len(board)
        n = len(board[0])
        dirs = [(-1,0),(1,0),(0,-1),(0,1),(-1,1),(1,1),(-1,-1),(1,-1)]
        die = []
        live = []
        for i in range(m):
            for j in range(n):
                cur = board[i][j]
                lived = 0
                if cur == 1:
                    for x,y in dirs:
                        ni = i+x
                        nj = j+y
                        if 0<=ni<m and 0<=nj<n:
                            if board[ni][nj] == 1:
                                lived += 1
                    if lived < 2 or lived > 3:
                        die.append((i,j))
                else:
                    for x,y in dirs:
                        ni = i+x
                        nj = j+y
                        if 0<=ni<m and 0<=nj<n:
                            if board[ni][nj] == 1:
                                lived += 1
                    if lived == 3:
                        live.append((i,j))
        for x,y in die:
            board[x][y] = 0
        for x,y in live:
            board[x][y] = 1