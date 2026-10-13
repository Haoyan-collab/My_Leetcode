class Solution:
    def twoSum(self, numbers: list[int], target: int) -> list[int]:
        n = len(numbers)
        cnt = {}

        for i,num in enumerate(numbers):
            fd = target - num
            if fd in cnt:
                return [cnt[fd],i+1]

            cnt[num] = i + 1

