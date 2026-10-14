class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        import heapq as hq
        q = []
        ans = []
        cnt = {}
        for n in nums:
            cnt[n] = cnt.get(n,0) + 1

        for n,times in cnt.items():
            hq.heappush(q,(times, n))
            if len(q) > k:
                hq.heappop(q)

        for tp in q:
            times, n = tp
            ans.append(n)

        return ans