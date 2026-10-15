class Solution:
    def trap(self, height: list[int]) -> int:
        ans = 0
        n = len(height)
        if n <= 2:
            return 0
        left, right = 0,n-1
        lmx, rmx = height[left], height[right]
        while left < right:
            while right > left and lmx >= rmx:
                right -= 1
                rmx = max(rmx, height[right])    
                ans += rmx - height[right]
                
            while left < right and lmx < rmx:
                left += 1
                lmx = max(lmx, height[left])
                ans += lmx - height[left]

                

        return ans 