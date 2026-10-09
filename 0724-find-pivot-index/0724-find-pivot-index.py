class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        sm = 0
        for s in nums:
            sm += s
        left, right = 0, 0
        for i, n in enumerate(nums):
            right = sm - left - n
            if left == right:
                return i
            left += n
        return -1

