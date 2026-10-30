from collections import Counter
class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        need = Counter(p)
        m = len(p)
        window = {}
        left,right = 0,0
        valid = 0
        ans = []
        while right<n:
            c = s[right]
            window[c] = window.get(c,0)+1
            right += 1
            if c in need:
                if window[c] == need[c]:
                    valid += 1
            if right-left > m:
                if s[left] in need and window[s[left]] == need[s[left]]:
                    valid -= 1
                window[s[left]] -= 1
                left += 1
            if right-left == m:
                if valid == len(need):
                    ans.append(left)
        return ans
