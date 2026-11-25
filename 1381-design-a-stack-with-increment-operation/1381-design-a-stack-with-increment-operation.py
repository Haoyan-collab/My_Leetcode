class CustomStack:

    def __init__(self, maxSize: int):
        self.size = maxSize
        self.sta = []
        self.inc = []

    def push(self, x: int) -> None:
        if len(self.sta)<self.size:
            self.sta.append(x)
            self.inc.append(0)

    def pop(self) -> int:
        if not self.sta:
            return -1
        s = self.sta.pop()
        i = self.inc.pop()
        if self.inc:
            self.inc[-1] += i
        return s+i

    def increment(self, k: int, val: int) -> None:
        i = min(len(self.sta),k)-1
        if i >= 0:
            self.inc[i] += val


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)