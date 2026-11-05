from collections import deque
class Solution:
    def maxSlidingWindow(self, nums: list[int], k: int) -> list[int]:
        q = deque()
        ans = []
        for i,n in enumerate(nums):
            while q and nums[q[-1]]<n:
                q.pop()
            q.append(i)
            while q and q[0]<i-k+1:
                q.popleft()
            if i>=k-1:
                ans.append(nums[q[0]])
        return ans