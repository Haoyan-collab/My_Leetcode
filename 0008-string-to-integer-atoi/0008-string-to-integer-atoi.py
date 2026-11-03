class Solution:
    def myAtoi(self, s: str) -> int:
        n = len(s)
        ans = 0
        idx = 0
        flag = False
        if s == "":
            return 0
        while idx<n and s[idx] == ' ':
            idx += 1
        print(idx,n)
        if idx<n and (s[idx] == '-' or s[idx] == '+'):
            if s[idx] == '-':
                flag = True
            idx += 1
        while idx<n and s[idx] == '0':
            idx += 1
        if idx < n and not s[idx].isdigit():
            return 0
        while idx<n and s[idx].isdigit():
            ans = 10*ans + int(s[idx])
            idx += 1
        if flag:
            ans = -ans
        if ans > 2**31 - 1:
            ans = 2**31 - 1
        elif ans < -2**31:
            ans = -2**31
        return ans