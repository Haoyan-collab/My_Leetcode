class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        prefix = {0:-1}
        ans = 0
        pfx = 0
        for i,n in enumerate(nums):
            if n == 0:
                pfx -= 1
            else:
                pfx += 1
            if pfx in prefix:
                ans = max(ans,i-prefix[pfx])
            else:
                prefix[pfx] = i
        return ans