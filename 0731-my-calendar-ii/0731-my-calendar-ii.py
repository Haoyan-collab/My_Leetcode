class MyCalendarTwo:

    def __init__(self):
        self.booked = []
        self.overlaps = []

    def book(self, startTime: int, endTime: int) -> bool:
        for i,j in self.overlaps:
            if startTime<j and endTime>i:
                return False
        
        for i,j in self.booked:
            if startTime<j and endTime>i:
                ml = max(startTime,i)
                mr = min(endTime,j)
                self.overlaps.append((ml,mr))
        self.booked.append((startTime,endTime))
        
        return True
        


# Your MyCalendarTwo object will be instantiated and called as such:
# obj = MyCalendarTwo()
# param_1 = obj.book(startTime,endTime)