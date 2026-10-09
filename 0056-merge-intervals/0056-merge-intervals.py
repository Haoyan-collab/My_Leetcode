class Solution:
    def merge(self, intervals: list[list[int]]) -> list[list[int]]:
        intervals.sort(key = lambda x: x[0])
        i, j = intervals[0][0], intervals[0][1]
        ans = []
        n = len(intervals)
        if n < 2:
            return intervals
        for k in range(1,n):
            x, y = intervals[k][0], intervals[k][1]
            if x > j:
                ans.append([i,j])
                i, j = x, y
                continue
            j = max(j, y)
        ans.append([i,j])
        return ans

