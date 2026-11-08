class MyCalendar:

    def __init__(self):
        self.q = []

    def book(self, startTime: int, endTime: int) -> bool:
        for i,j in self.q:
            if startTime<j and endTime>i:
                return False
        self.q.append((startTime,endTime))
        return True
        


# Your MyCalendar object will be instantiated and called as such:
# obj = MyCalendar()
# param_1 = obj.book(startTime,endTime)