class Solution:
    def partition(self, s: str) -> list[list[str]]:
        def is_pa(s):
            n = len(s)
            if n%2 == 0:
                left,right = n//2 - 1, n//2
                while 0<=left and right<n:
                    if s[left] != s[right]:
                        return False
                    left -= 1
                    right += 1
                return True
            else:
                left,right = n//2, n//2
                while 0<=left and right<n:
                    if s[left] != s[right]:
                        return False
                    left -= 1
                    right += 1
                return True
        
        ans = []
        def dfs(i,path):
            if i == len(s):
                ans.append(path.copy())
                return
            for j in range(i+1,len(s)+1):
                if is_pa(s[i:j]):
                    path.append(s[i:j])
                    dfs(j,path)
                    path.pop()
        path = []
        dfs(0,path)
        return ans