class Solution:
    def longestPalindrome(self, s: str) -> str:
        n = len(s)
        length = 0
        ans = []
        for i in range(n):
            # odd
            left,right = i,i
            while 0<=left<n and 0<=right<n and s[left] == s[right]:
                if right-left+1 > length:
                    length = right-left+1
                    ans = [left,right]
                left -= 1
                right += 1
            
            # even
            left,right = i,i+1
            while 0<=left<n and 0<=right<n and s[left] == s[right]:
                if right-left+1 > length:
                    length = right-left+1
                    ans = [left,right]
                left -= 1
                right += 1
        i,j = ans
        return s[i:j+1]
                