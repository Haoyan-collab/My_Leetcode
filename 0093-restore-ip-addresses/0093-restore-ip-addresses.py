class Solution:
    def restoreIpAddresses(self, s: str) -> list[str]:
        ans = []
        n = len(s)
        def dfs(i,path):
            nonlocal ans
            if i == n and len(path)==4:
                ans.append('.'.join(path))
                return
            for j in range(i+1,min(n,i+3)+1):
                p = s[i:j]
                if len(p)>1 and p[0]=='0':
                    continue
                if int(p)>255:
                    continue
                path.append(p)
                dfs(j,path)
                path.pop()
        
        dfs(0,[])
        return ans