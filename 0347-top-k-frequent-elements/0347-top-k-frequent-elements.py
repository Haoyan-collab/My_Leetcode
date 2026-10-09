class Solution:
    def topKFrequent(self, nums: list[int], k: int) -> list[int]:
        import heapq as hp
        cnt = defaultdict(int)
        for n in nums:
            cnt[n] += 1
        heap = []
        for num,times in cnt.items():
            hp.heappush(heap,(times,num))
            if len(heap) > k:
                hp.heappop(heap)
        ans = []
        for times,num in heap:
            ans.append(num)
        return ans