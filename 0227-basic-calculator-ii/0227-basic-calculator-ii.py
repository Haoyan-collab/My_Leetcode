class Solution:
    def calculate(self, s: str) -> int:
        ans = 0
        op = '+'
        sta = []
        for i,c in enumerate(s):
            if c.isdigit():
                ans = ans*10 + int(c)
            if c in '+-*/' or i==len(s)-1:
                if op == '+':
                    sta.append(ans)
                if op == '-':
                    sta.append(-ans)
                if op == '*':
                    sta.append(sta.pop()*ans)
                if op == '/':
                    sta.append(int(sta.pop()/ans))
                op = c
                ans = 0

        return sum(sta)