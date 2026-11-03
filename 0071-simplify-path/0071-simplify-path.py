class Solution:
    def simplifyPath(self, path: str) -> str:
        sta = []
        n = len(path)
        left,right =0,0
        while right < n:
            while right < n and path[right] == '/':
                right += 1
            left = right
            if right == n:
                break
            while right < n and path[right] != '/':
                right += 1
            cur = path[left:right]
            print(cur)
            if cur == '.':
                continue
            elif cur == '..':
                if sta:
                    sta.pop()
            else:
                sta.append(cur)
        
        return "/" + "/".join(sta)