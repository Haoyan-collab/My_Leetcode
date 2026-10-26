class Solution:
    def insert(self, intervals: list[list[int]], newInterval: list[int]) -> list[list[int]]:
        nl,nr = newInterval
        i = 0
        n = len(intervals)
        ans = []
        while i<n and intervals[i][1] < nl:
            ans.append(intervals[i])
            i += 1
        while i<n and intervals[i][0] <= nr:
            nl = min(nl,intervals[i][0])
            nr = max(nr,intervals[i][1])
            i += 1
        ans.append([nl,nr])
        while i<n:
            ans.append(intervals[i])
            i += 1
        return ans