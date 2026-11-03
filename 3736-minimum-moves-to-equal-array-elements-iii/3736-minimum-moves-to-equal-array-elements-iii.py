class Solution:
    def minMoves(self, nums: List[int]) -> int:
        mx = max(nums)
        ans = 0
        for n in nums:
            ans += mx-n
        return ans