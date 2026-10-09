class Solution:
    import math
    def minSubArrayLen(self, target: int, nums: list[int]) -> int:
        sm = 0
        n = len(nums)
        ans = n + 1
        left, right = 0, 0
        while right < n:
            sm += nums[right]
            right += 1
            if sm >= target:
                while sm >= target and left < right:
                    sm -= nums[left]
                    left += 1
                ans = min(right - left + 1, ans)
        return 0 if ans == n + 1 else ans