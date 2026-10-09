class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        cnt = set()
        ans = 0
        left, right = 0,0
        n = len(s)
        while right < n:
            if s[right] in cnt:
                while s[right] in cnt and left <= right:
                    cnt.remove(s[left])
                    left += 1
            cnt.add(s[right])
            right += 1
            ans = max(right - left, ans)
        return ans