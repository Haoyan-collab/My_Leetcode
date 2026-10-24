class Solution:
    def eraseOverlapIntervals(self, intervals: list[list[int]]) -> int:
        intervals.sort(key = lambda x:x[0])
        ans = 0
        sta = [intervals[0]]
        for i in range(1,len(intervals)):
            cl,cr = sta[-1]
            nl,nr = intervals[i]
            if nl >= cr:
                sta.append(intervals[i])
                continue
            ans += 1
            if nr > cr:
                continue
            else:
                sta.pop()
                sta.append(intervals[i])

        return ans