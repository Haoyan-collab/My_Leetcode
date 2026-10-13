class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        nums = set(nums)
        nums = list(nums)
        nums.sort()
        n = len(nums)
        ans = 0
        left, right = 0,0
        while right < n:
            while right < n-1 and nums[right+1] == nums[right]+1:
                right += 1
            ans = max(ans, right - left + 1)
            right += 1
            left = right

        return ans