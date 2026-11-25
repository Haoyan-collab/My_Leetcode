from collections import deque
class Solution:
    def canVisitAllRooms(self, rooms: list[list[int]]) -> bool:
        n = len(rooms)
        q = deque()
        visited = {0:1}
        for k in rooms[0]:
            q.append(k)
        while q:
            cur = q.pop()
            if cur not in visited:
                visited[cur] = 1
                for k in rooms[cur]:
                    q.append(k)
        if len(visited) == n:
            return True
        return False