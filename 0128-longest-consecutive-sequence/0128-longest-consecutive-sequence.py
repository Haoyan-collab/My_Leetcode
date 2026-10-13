class Solution:
    def longestConsecutive(self, nums: list[int]) -> int:
        cnt = set(nums)
        ans = 0

        for num in cnt:
            if num - 1 not in cnt:
                length = 1
                while num + length in cnt:
                    length += 1

                ans = max(length, ans)

        return ans