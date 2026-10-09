class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        # easiest way
        #return sorted(s) == sorted(t)
        cnt = defaultdict(int)
        if len(s) != len(t):
            return False
        for c in s:
            cnt[c] += 1
        
        for c in t:
            if c not in cnt:
                return False
            cnt[c] -= 1
            if cnt[c] == 0:
                cnt.pop(c)
        return True