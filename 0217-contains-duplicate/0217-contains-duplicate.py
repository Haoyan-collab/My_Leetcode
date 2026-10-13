class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # easiest
        return not (len(set(nums)) == len(nums))