class Solution:
    def partitionLabels(self, s: str) -> list[int]:
        ans = []
        fst = {}
        lst = {}
        for i,c in enumerate(s):
            if c not in fst:
                fst[c] = i
            lst[c] = i
        n = len(s)
        left, right = 0,0
        while right < n:
            c = s[left]
            right = lst[c]
            i = left + 1
            while i < right:
                c = s[i]
                if lst[c] > right:
                    right = lst[c]
                i += 1
            ans.append(right-left+1)
            right += 1
            left = right
        return ans