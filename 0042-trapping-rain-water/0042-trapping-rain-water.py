from collections import deque
class Solution:
    def trap(self, height: list[int]) -> int:
        q = deque()
        ans = 0
        n = len(height)
        if n <= 2:
            return 0
        i = 0
        while i < n:
            h = height[i]
            while q and height[q[-1]] < h:
                cur = q.pop()
                if q:
                    length = i - q[-1] - 1
                    ans += length * (min(h,height[q[-1]])-height[cur])
            q.append(i)
            i += 1

        return ans
        # two pointers
        # ans = 0
        # n = len(height)
        # if n <= 2:
        #     return 0
        # left, right = 0,n-1
        # lmx, rmx = height[left], height[right]
        # while left < right:
        #     while right > left and lmx >= rmx:
        #         right -= 1
        #         rmx = max(rmx, height[right])    
        #         ans += rmx - height[right]
                
        #     while left < right and lmx < rmx:
        #         left += 1
        #         lmx = max(lmx, height[left])
        #         ans += lmx - height[left]
        # return ans 