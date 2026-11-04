class Solution:
    def minDays(self, bloomDay: list[int], m: int, k: int) -> int:
        n = len(bloomDay)
        if n < m*k:
            return -1
        
        def canMake(d):
            nonlocal m
            cnt = 0
            left,right = 0,0
            for right in range(n):
                if bloomDay[right] > d:
                    length = right-left
                    cnt += length//k
                    left = right+1
            return m <= cnt + (n-left)//k
        
        l,r = min(bloomDay),max(bloomDay)
        while l<=r:
            mid = (l+r)//2
            if canMake(mid):
                r = mid-1
            else:
                l = mid+1
        return l