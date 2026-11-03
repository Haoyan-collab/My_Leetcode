from collections import deque
class Solution:
    def snakesAndLadders(self, board: list[list[int]]) -> int:
        n = len(board)
        def index(num):
            nonlocal n
            res = (num-1)%n
            k = (num-1)//n
            i = n-k-1
            j = res
            if k%2 == 1:
                j = n-res-1
            return (i,j)
        
        steps = 0
        q = deque()
        q.append(1)
        visited = {1:1}
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur == n**2:
                    return steps
                for i in range(cur+1,min(cur+7,n**2+1)):
                    r,c = index(i)
                    if board[r][c] != -1:
                        if board[r][c] not in visited:
                            visited[board[r][c]] = 1
                            q.append(board[r][c])
                    else:
                        if i not in visited:
                            visited[i] = 1
                            q.append(i)
            steps += 1
        
        return -1