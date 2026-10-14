class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        ans = 0
        n = len(s)
        left, right = 0,0
        cnt = {}
        mx = 0
        while right < n:
            cnt[s[right]] = cnt.get(s[right],0) + 1
            mx = max(mx, cnt[s[right]])
            right += 1
            length = right - left
            # u dont need to update mx for this while loop! it'll work
            while length - mx > k:
                cnt[s[left]] = cnt.get(s[left],0) - 1
                left += 1
                length = right - left

            ans = max(ans, length)

        return ans
