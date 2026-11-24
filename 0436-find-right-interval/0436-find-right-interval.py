class Solution:
    def findRightInterval(self, intervals: list[list[int]]) -> list[int]:
        n = len(intervals)
        start = sorted((s,i) for i,(s,e) in enumerate(intervals))
        ans = []
        for _,e in intervals:
            l,r = 0,n
            while l<r:
                m = (l+r)//2
                if start[m][0]>=e:
                    r = m
                else:
                    l = m+1
            if l == n:
                ans.append(-1)
            else:
                ans.append(start[l][1])
        
        return ans
        