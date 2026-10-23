from collections import defaultdict
from collections import deque
class Solution:
    def networkDelayTime(self, times: list[list[int]], n: int, k: int) -> int:
        graph = defaultdict(list)
        for edge in times:
            src,dst,w = edge
            graph[src].append((dst,w))
        ans = float('inf')
        dist = {i:float('inf') for i in range(1,n+1)}
        dist[k] = 0
        q = deque()
        q.append((k,0))
        while q:
            cur,t = q.popleft()
            if t > dist[cur]:
                continue
            for dst,w in graph[cur]:
                if dist[dst] > t+w:
                    dist[dst] = t+w
                    q.append((dst,t+w))
        ans = max(dist.values())
        return ans if ans!=float('inf') else -1