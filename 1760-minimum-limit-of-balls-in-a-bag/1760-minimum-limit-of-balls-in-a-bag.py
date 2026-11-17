class Solution:
    def minimumSize(self, nums: list[int], maxOperations: int) -> int:
        nums = sorted(nums)[::-1]
        def fit(p):
            cnt = 0
            num = nums
            for n in num:
                if cnt<=maxOperations and n<=p:
                    return True
                cnt += (n-1)//p
                if cnt>maxOperations:
                    return False
            if cnt<=maxOperations:
                return True

        l,r = 1,nums[0]+1
        while l<r:
            m = (l+r)//2
            if fit(m):
                r = m
            else:
                l = m+1
        return r
