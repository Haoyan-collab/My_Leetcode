from collections import Counter
class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        m = len(word1)
        n = len(word2)
        if m!=n:
            return False
        
        cnt1 = Counter(word1)
        cnt2 = Counter(word2)
        if cnt1 == cnt2:
            return True
        c1 = [c for c in cnt1.keys()]
        c2 = [c for c in cnt2.keys()]
        v1 = [v for v in cnt1.values()]
        v2 = [v for v in cnt2.values()]
        if Counter(v1) == Counter(v2) and Counter(c1)==Counter(c2):
            return True
        
        return False
        

