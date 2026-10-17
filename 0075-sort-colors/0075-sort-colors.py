class Solution:
    def sortColors(self, nums: list[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        n = len(nums)
        zero,cur,twos = 0,0,n-1
        while cur <= twos:
            num = nums[cur]
            if num == 0:
                nums[cur],nums[zero] = nums[zero],nums[cur]
                zero += 1
                cur += 1
                continue
            elif num == 2:
                nums[cur],nums[twos] = nums[twos],nums[cur]
                twos -= 1
                continue
            cur += 1
        