class Solution:
    def maxDiff(self, num: int) -> int:
        x = None
        num = str(num)
        for n in num:
            if n != '9':
                x = n
                break
        mx = []
        if x :
            for n in num:
                if n == x:
                    mx.append('9')
                else:
                    mx.append(n)
        else:
            mx = num
        mx = int("".join(mx))


        idx = 0
        x = None
        if num[0] == '1':
            for i in range(1,len(num)):
                n = num[i]
                if n != '0' and n != '1':
                    idx = i
                    x = n
                    break
        else:
            idx = 0
            x = num[0]
        mi = []
        y = '0' if idx!=0 else '1'
        if x:
            for n in num:
                if n == x:
                    mi.append(y)
                else:
                    mi.append(n)
        else:
            mi = num

        mi = int("".join(mi))
        return mx-mi

        