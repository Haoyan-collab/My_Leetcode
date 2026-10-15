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
                print("rmx:",rmx,"right:",right,"ans",ans)
                

            while left < right and lmx < rmx:
                left += 1
                lmx = max(lmx, height[left])
                ans += lmx - height[left]
                print("lmx:",lmx,"left:",left,"ans",ans)
                

        return ans 