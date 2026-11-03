import heapq as hp
class MedianFinder:

    def __init__(self):
        self.small = []
        self.large = []

    def addNum(self, num: int) -> None:
        hp.heappush(self.small,-num)
        if self.large and -self.small[0] > self.large[0]:
            val = -hp.heappop(self.small)
            hp.heappush(self.large,val)
        
        if len(self.small) > len(self.large)+1:
            val = -hp.heappop(self.small)
            hp.heappush(self.large,val)
        
        if len(self.small) < len(self.large):
            val = hp.heappop(self.large)
            hp.heappush(self.small,-val)
        
        return None

    def findMedian(self) -> float:
        if (len(self.small)+len(self.large))%2 == 0:
            return (-self.small[0]+self.large[0])/2
        else:
            return -self.small[0]

# Your MedianFinder object will be instantiated and called as such:
# obj = MedianFinder()
# obj.addNum(num)
# param_2 = obj.findMedian()