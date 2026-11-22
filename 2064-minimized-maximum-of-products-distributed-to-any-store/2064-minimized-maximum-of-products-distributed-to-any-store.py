class Solution:
    def minimizedMaximum(self, n: int, quantities: list[int]) -> int:
        def fit(x):
            cnt = 0
            for q in quantities:
                if q%x == 0:
                    cnt += q//x
                else:
                    cnt += q//x + 1
                if cnt > n:
                    return False
            return True
        
        l,r = 1,max(quantities)+1
        while l<r:
            m = (l+r)//2
            if fit(m):
                r = m
            else:
                l = m+1
        return l