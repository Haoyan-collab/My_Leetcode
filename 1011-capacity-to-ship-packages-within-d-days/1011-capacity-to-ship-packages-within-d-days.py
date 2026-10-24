class Solution:
    def shipWithinDays(self, weights: list[int], days: int) -> int:
        sm = 0
        max_w = 0
        for w in weights:
            sm += w
            max_w = max(max_w,w)
        left, right = max_w, sm
        while left <= right:
            mid = (left+right)//2
            day = 0
            i = 0
            while i < len(weights):
                w1d = 0
                while i<len(weights) and w1d + weights[i] <= mid:
                    w1d += weights[i]
                    i+= 1
                day += 1

            if day > days:
                left = mid+1
            else:
                right = mid - 1
        
        return left