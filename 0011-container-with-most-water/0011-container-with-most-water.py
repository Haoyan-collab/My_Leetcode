class Solution:
    def maxArea(self, height: list[int]) -> int:
        n = len(height)
        left, right = 0, n-1
        ans = 0
        while left < right:
            length = right - left
            space = length * min(height[left], height[right])
            ans = max(space, ans)
            if height[left] <= height[right]:
                left += 1
                while left < right and height[left] < height[left - 1]:
                    left += 1
            else:
                right -= 1
                while left < right and height[right] < height[right + 1]:
                    right -= 1
        return ans