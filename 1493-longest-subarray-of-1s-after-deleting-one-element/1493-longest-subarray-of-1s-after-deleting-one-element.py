class Solution:
    def longestSubarray(self, nums: list[int]) -> int:
        n = len(nums)
        l,r = 0,0
        cnt = 0
        ans = 0
        while r<n:
            if nums[r] == 0:
                cnt += 1
            while cnt==2:
                if nums[l]==0:
                    cnt-=1
                l += 1
            r += 1
            ans = max(ans,r-l-1)
            
        return ans