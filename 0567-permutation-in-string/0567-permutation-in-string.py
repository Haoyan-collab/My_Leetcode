class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        cnt = {}
        for s in s1:
            cnt[s] = cnt.get(s,0)+1
        
        n = len(s2)
        left, right = 0,0
        for right in range(n):
            cnt[s2[right]] = cnt.get(s2[right],0)-1
            if right-left+1 > len(s1):
                cnt[s2[left]] = cnt.get(s2[left],0)+1
                left += 1
            if right-left+1 == len(s1):
                if all(val==0 for val in cnt.values()):
                    return True
        
        return False