class Solution:
    def intervalIntersection(self, firstList: list[list[int]], secondList: list[list[int]]) -> list[list[int]]:
        m = len(firstList)
        n = len(secondList)
        if m == 0 or n == 0:
            return []
        
        ans = []
        for i,lengthb in enumerate(secondList):
            lb = lengthb[0]
            rb = lengthb[1]
            j = 0
            while j < m and (firstList[j][1]<lb):
                j += 1

            # if firstList[j][0] > rb:
            #     continue
            while j<m and firstList[j][0] <= rb:
                ans.append([max(firstList[j][0],lb),min(firstList[j][1],rb)])
                j += 1
        return ans