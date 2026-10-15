class Solution:
    def findKthLargest(self, nums: list[int], k: int) -> int:
        import heapq as hp
        q = []
        for n in nums:
            hp.heappush(q,n)
            if len(q) > k:
                hp.heappop(q)
        return q[0]
