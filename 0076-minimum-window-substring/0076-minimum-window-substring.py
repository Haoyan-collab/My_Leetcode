class Solution:
    def minWindow(self, s: str, t: str) -> str:
        m = len(s)
        n = len(t)
        if n > m:
            return ""

        idx = ()
        ans = float('inf')
        tcnt = {}
        for c in t:
            tcnt[c] = tcnt.get(c,0) + 1

        target = len(tcnt)
        window = {}
        cur = 0
        left, right = 0, 0
        while right < m:
            rt = s[right]
            window[rt] = window.get(rt,0) + 1
            right += 1
            if rt in tcnt and tcnt[rt] == window[rt]:
                cur += 1
                if cur == target:
                    while cur == target:
                        lt = s[left]
                        window[lt] = window.get(lt,0) - 1
                        if lt in tcnt and tcnt[lt] > window[lt]:
                            cur -= 1
                        left += 1
                    
                    length = right - left + 1
                    if length < ans:
                        ans = length
                        idx = (left-1,right)

        if ans == float('inf'):
            return ""
        i,j = idx

        return "".join(s[i:j])