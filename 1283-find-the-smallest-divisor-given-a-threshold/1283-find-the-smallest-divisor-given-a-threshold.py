class Solution:
    def smallestDivisor(self, nums: list[int], threshold: int) -> int:
        n = len(nums)
        l,r = 1,max(nums)+1

        def fit(d):
            cnt = 0
            for n in nums:
                r = n//d if n%d==0 else n//d + 1
                cnt += r
            return cnt<=threshold
        
        while l<r:
            m = (l+r)//2
            if fit(m):
                r = m
            else:
                l = m+1
        
        return l
