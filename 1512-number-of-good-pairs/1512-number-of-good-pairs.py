class Solution:
    def numIdenticalPairs(self, nums: list[int]) -> int:
        cnt = defaultdict(int)
        ans = 0
        for i,n in enumerate(nums):
            if n in cnt:
                ans += cnt[n]
            cnt[n] += 1
        return ans