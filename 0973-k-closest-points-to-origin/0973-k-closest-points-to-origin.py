class Solution:
    def kClosest(self, points: list[list[int]], k: int) -> list[list[int]]:
        import math
        import heapq as hq
        heap = []
        ans = []
        for p in points:
            dis = math.sqrt(p[0]**2 + p[1]**2)
            hq.heappush(heap,(-dis,p))
            if len(heap) > k:
                hq.heappop(heap)
        for _,(dis,p) in enumerate(heap):
            ans.append(p)
        return ans