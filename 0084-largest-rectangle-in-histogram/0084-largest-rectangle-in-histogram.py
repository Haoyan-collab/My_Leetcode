class Solution:
    def largestRectangleArea(self, heights: list[int]) -> int:
        sta = []
        ans = 0
        for i,h in enumerate(heights):
            while sta and h<heights[sta[-1]]:
                cur = sta.pop()
                left = sta[-1] if sta else -1
                length = i-left-1
                ans = max(ans,heights[cur]*length)
            sta.append(i)
        while sta:
            cur = sta.pop()
            left = sta[-1] if sta else -1
            length = len(heights)-left-1
            ans = max(ans,heights[cur]*length)
        return ans