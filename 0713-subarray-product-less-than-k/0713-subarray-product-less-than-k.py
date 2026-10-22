class Solution:
    def numSubarrayProductLessThanK(self, nums: list[int], k: int) -> int:
        n = len(nums)
        left, right = 0,0
        prodsm = 1
        ans = 0
        while right < n:
            prodsm *= nums[right]

            while left <= right and prodsm >= k:
                prodsm /= nums[left]
                left += 1
            ans += right-left+1
            right += 1
        return ans