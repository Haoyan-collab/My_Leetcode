class Solution:
    def decodeString(self, s: str) -> str:
        cur = ''
        num = 0
        stack = []
        for c in s:
            if c.isalpha():
                cur += c
            elif c.isdigit():
                num = num*10 + int(c)
            elif c == '[':
                stack.append((cur,num))
                cur = ''
                num = 0
            else:
                prev,times = stack.pop()
                cur = prev + times*cur
        return cur