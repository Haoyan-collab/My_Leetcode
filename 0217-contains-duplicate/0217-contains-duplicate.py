class Solution:
    def containsDuplicate(self, nums: list[int]) -> bool:
        # easiest
        # return not (len(set(nums)) == len(nums))

        # hashmap
        cnt = {}
        for n in nums:
            if n in cnt:
                return True

            cnt[n] = 1

        return False