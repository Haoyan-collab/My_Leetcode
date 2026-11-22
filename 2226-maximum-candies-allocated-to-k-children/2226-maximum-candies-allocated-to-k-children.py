class Solution:
    def maximumCandies(self, candies: list[int], k: int) -> int:
        def fit(x):
            cnt = 0
            for c in candies:
                cnt += c//x
                if cnt >= k:
                    return True
            return False
        
        l,r = 1,sum(candies)+1
        if r<k:
            return 0
        while l<r:
            m = (l+r)//2
            if fit(m):
                l = m+1
            else:
                r = m
        
        return l-1