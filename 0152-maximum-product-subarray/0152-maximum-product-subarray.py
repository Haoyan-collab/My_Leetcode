class Solution:
    def maxProduct(self, nums: list[int]) -> int:
        dp_min,dp_max = [n for n in nums],[n for n in nums]
        if len(nums) == 1:
            return nums[0]
        for i in range(1,len(nums)):
            dp_min[i] = min(dp_min[i],dp_min[i-1]*nums[i],dp_max[i-1]*nums[i])
            dp_max[i] = max(dp_max[i],dp_min[i-1]*nums[i],dp_max[i-1]*nums[i])
        return max(dp_max)