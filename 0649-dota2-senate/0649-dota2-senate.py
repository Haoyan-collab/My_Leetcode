class Solution:
    def predictPartyVictory(self, senate: str) -> str:
        #cnt of r and d: if d == 0, return r, else: d -= 1
        from collections import deque
        r = deque()
        d = deque()
        n = len(senate)
        for i,s in enumerate(senate):
            if s == 'R':
                r.append(i)
            else:
                d.append(i)
        while r and d:
            rt = r.popleft()
            dt = d.popleft()

            if rt < dt:
                r.append(rt + n)
            else:
                d.append(dt + n)
        return "Radiant" if r else "Dire"
        