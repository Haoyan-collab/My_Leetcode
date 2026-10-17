import math
import heapq
class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        q = []
        for x,y in points:
            distance = math.sqrt(x**2 + y**2)
            heapq.heappush(q,(-distance,(x,y)))
            if len(q) > k:
                heapq.heappop(q)
        ans = []
        for _,co in q:
            x,y = co
            ans.append([x,y])
        return ans