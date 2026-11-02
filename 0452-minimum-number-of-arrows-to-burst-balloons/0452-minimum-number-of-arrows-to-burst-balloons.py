class Solution:
    def findMinArrowShots(self, points: list[list[int]]) -> int:
        points = sorted(points,key=lambda x:x[0])
        n = len(points)
        ans = 0
        left,right = 0,0
        nl,nr = points[0]
        for right in range(1,n):
            cur = points[right]
            nl,nr = max(nl,cur[0]), min(nr,cur[1])
            if nl > nr:
                ans += 1
                nl,nr = cur
        return ans+1
            