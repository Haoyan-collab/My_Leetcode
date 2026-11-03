import heapq as hp
class KthLargest:

    def __init__(self, k: int, nums: list[int]):
        self.q = []
        self.k = k
        for n in nums:
            hp.heappush(self.q,n)
            if len(self.q)>self.k:
                hp.heappop(self.q)

    def add(self, val: int) -> int:
        hp.heappush(self.q,val)
        if len(self.q) > self.k:
            hp.heappop(self.q)
        return self.q[0]

# Your KthLargest object will be instantiated and called as such:
# obj = KthLargest(k, nums)
# param_1 = obj.add(val)