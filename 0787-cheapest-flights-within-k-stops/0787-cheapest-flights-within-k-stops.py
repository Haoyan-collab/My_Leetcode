from collections import deque
class Solution:
    def findCheapestPrice(self, n: int, flights: list[list[int]], src: int, dst: int, k: int) -> int:
        distance = [float('inf')]*n
        distance[src] = 0
        snapshot = []
        for _ in range(k+1):
            snapshot = distance.copy()
            updated = False
            for i,j,w in flights:
                if snapshot[i] != float('inf'):
                    if distance[j] > snapshot[i]+w:
                        distance[j] = snapshot[i]+w
                        updated = True
            if not updated:
                break
        return distance[dst] if distance[dst] != float('inf') else -1