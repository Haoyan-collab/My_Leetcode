from collections import deque
class Solution:
    def shortestAlternatingPaths(self, n: int, redEdges: list[list[int]], blueEdges: list[list[int]]) -> list[int]:
        graph = [[[] for _ in range(n)] for _ in range(2)]
        # current_red
        for u,v in redEdges:
            graph[0][u].append(v)
        # current_blue
        for u,v in blueEdges:
            graph[1][u].append(v)

        dist = [[float('inf')]*2 for _ in range(n)]
        print(dist)
        dist[0] = [0,0]
        q = deque()
        q.append((0,0))
        q.append((0,1))
        while q:
            node,stat = q.popleft()
            next_stat = 1 - stat
            for n in graph[next_stat][node]:
                if dist[n][next_stat] == float('inf'):
                    dist[n][next_stat] = 1 + dist[node][stat]
                    q.append((n,next_stat))
        ans = []
        for d in dist:
            m = min(d)
            if m != float('inf'):
                ans.append(m)
            else:
                ans.append(-1)
        return ans