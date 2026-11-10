class Solution:
    def minSpeedOnTime(self, dist: list[int], hour: float) -> int:

        l,r = 1,10**7
        def arrived(s):
            times = 0
            for i,d in enumerate(dist):
                if i < len(dist)-1:
                    times += (d+s-1)//s

                else:
                    times += d/s

            if times <= hour:
                return True
            return False

        while l<r:
            m = (l+r)//2
            if arrived(m):
                r = m
            else:
                l = m+1
        if not arrived(r):
            return -1
        return r
