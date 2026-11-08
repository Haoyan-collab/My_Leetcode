class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        sta = []
        lft = []
        for i,c in enumerate(s):
            if c == '(':
                sta.append(i)
            elif c == ')':
                if sta:
                    sta.pop()
                else:
                    lft.append(i)
        
        remove = set(sta+lft)
        return "".join(c for i,c in enumerate(s) if i not in remove)