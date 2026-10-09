class Solution:
    def findAnagrams(self, s: str, p: str) -> list[int]:
        n = len(s)
        m = len(p)
        target = [0] * 26
        window = [0] * 26
        ans = []
        for c in p:
            target[ord(c) - ord('a')] += 1

        left, right = 0, 0
        for right in range(n):
            c = s[right]
            window[ord(c) - ord('a')] += 1
            # sliding window, keep window with fixed length m
            if right >= m:
                d = s[left]
                window[ord(d) - ord('a')] -= 1
                left += 1
            if right - left + 1 == m: # check the anagram
                if window == target:
                    ans.append(left)
        
        return ans

