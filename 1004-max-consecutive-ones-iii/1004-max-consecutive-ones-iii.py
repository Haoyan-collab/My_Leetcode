class Solution:
    def longestOnes(self, nums: list[int], k: int) -> int:
        sm = 0
        n = len(nums)
        left,right = 0,0
        ans = 0
        while right < n:
            sm += nums[right]
            right += 1
            while left<right and right-left>sm+k:
                sm -= nums[left]
                left += 1
            ans = max(ans,right-left)
        return ans