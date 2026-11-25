import heapq as hp
class Solution:
    def findClosestElements(self, arr: List[int], k: int, x: int) -> List[int]:
        q = []
        for a in arr:
            hp.heappush(q,(-abs(a-x),-a))
            if len(q) > k:
                hp.heappop(q)
        ans = []
        for _ in range(k):
            length,a = hp.heappop(q)
            ans.append(-a)
        return sorted(ans)