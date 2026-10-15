class MinStack:

    def __init__(self):
        self.lst = []
        self.minsta = []
    def push(self, value: int) -> None:
        self.lst.append(value)
        if not self.minsta:
            self.minsta.append(value)
        else:
            self.minsta.append(min(self.minsta[-1],value))
    def pop(self) -> None:
        self.lst.pop()
        self.minsta.pop()
    def top(self) -> int:
        return self.lst[-1]

    def getMin(self) -> int:
        return self.minsta[-1]


# Your MinStack object will be instantiated and called as such:
# obj = MinStack()
# obj.push(value)
# obj.pop()
# param_3 = obj.top()
# param_4 = obj.getMin()