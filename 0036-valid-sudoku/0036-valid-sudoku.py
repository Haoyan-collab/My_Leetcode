class Solution:
    def isValidSudoku(self, board: list[list[str]]) -> bool:
        for i in range(9):
            cnt = {}
            for j in range(9):
                if board[i][j] in cnt:
                    return False
                if board[i][j] != '.':
                    cnt[board[i][j]] = 1

        for j in range(9):
            cnt = {}
            for i in range(9):
                if board[i][j] in cnt:
                    return False
                if board[i][j] != '.':
                    cnt[board[i][j]] = 1

        for i,j in [(0,0),(3,0),(6,0),(0,3),(3,3),(6,3),(0,6),(3,6),(6,6)]:
            cnt = {}
            for x in range(i,i+3):
                for y in range(j,j+3):
                    if board[x][y] in cnt:
                        return False
                    if board[x][y] != '.':
                        cnt[board[x][y]] = 1

        return True