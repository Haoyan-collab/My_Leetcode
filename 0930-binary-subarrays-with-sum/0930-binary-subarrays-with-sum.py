class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        prefix = 0
        cnt = {0:1}
        ans = 0
        for n in nums:
            prefix += n
            target = prefix - goal
            if target in cnt:
                ans += cnt[target]
            cnt[prefix] = cnt.get(prefix,0)+1
        return ans