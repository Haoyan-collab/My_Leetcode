class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        m = len(firstList)
        n = len(secondList)
        if m == 0 or n == 0:
            return []
        
        ans = []
        a, b = 0,0
        while a < m and b < n:
            a1,a2 = firstList[a]
            b1,b2 = secondList[b]
            left = max(a1,b1)
            right = min(a2,b2)
            if left <= right:
                ans.append([left,right])
            if a2 < b2:
                a += 1
            else:
                b += 1
        return ans