class Solution:
    def maxDistance(self, position: list[int], m: int) -> int:
        n = len(position)
        position = sorted(position)
        ans = 0
        l,r = 1, position[-1]-position[0]+1

        def canPut(force):
            cnt = 1
            cur = position[0]
            for p in position[1:]:
                if p-cur>=force:
                    cnt += 1
                    cur = p
                    if cnt==m:
                        return True
            return False

        while l<r:
            mid = (l+r)//2
            if canPut(mid):
                l = mid+1
            else:
                r = mid
        return l-1
