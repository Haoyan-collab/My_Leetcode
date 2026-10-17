class Solution:
    def moveZeroes(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        ze,nonze = 0,0
        while nonze < n:
            if nums[nonze] != 0:
                nums[ze], nums[nonze] = nums[nonze], nums[ze]
                ze += 1
            nonze += 1
