class UndergroundSystem:

    def __init__(self):
        self.check_in = defaultdict(list)  # id -> station,time
        self.times = defaultdict(int)     # trace -> times
        self.totalTime = defaultdict(int) # trace -> totaltime
    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.check_in[id] = [stationName, t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        [start_station, start_time] = self.check_in.pop(id)
        total_time = t - start_time
        trace = (start_station, stationName)
        self.totalTime[trace] += total_time
        self.times[trace] += 1

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        trace = (startStation, endStation)
        return self.totalTime[trace] / self.times[trace]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)