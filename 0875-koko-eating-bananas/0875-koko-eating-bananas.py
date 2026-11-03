class Solution:
    def minEatingSpeed(self, piles: list[int], h: int) -> int:
        def couldfinish(k):
            hours = 0
            for p in piles:
                hours += (p+k-1)//k
            return hours <= h
        left, right = 1, max(piles)
        mid = 0
        while left <= right:
            mid = (left+right)//2
            if couldfinish(mid):
                right = mid - 1
            else:
                left = mid + 1
        return left
