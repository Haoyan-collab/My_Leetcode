class Solution:
    def maxDiff(self, num: int) -> int:
        
        num = str(num)
        # max
        x = next((c for c in num if c != '9'),'9')
        mx = int(num.replace(x,'9'))

        # min
        if num[0] != '1':
            mi = int(num.replace(num[0],'1'))
        else:
            x = next((c for c in num[1:] if c not in '01'),'0')
            mi = int(num.replace(x,'0'))
        return mx-mi

        