class StockSpanner:

    def __init__(self):
        self.q = []
        self.d = 0
    def next(self, price: int) -> int:
        while self.q and self.q[-1][0]<=price:
            self.q.pop()
        self.q.append((price,self.d))
        self.d += 1

        if len(self.q)==1:
            return self.d
        return self.q[-1][1]-self.q[-2][1]


# Your StockSpanner object will be instantiated and called as such:
# obj = StockSpanner()
# param_1 = obj.next(price)