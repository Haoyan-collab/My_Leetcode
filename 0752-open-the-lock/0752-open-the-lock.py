from collections import Counter, deque
class Solution:
    def openLock(self, deadends: list[str], target: str) -> int:
        s = "0000"
        dead = Counter(deadends)
        q = deque()
        q.append(s)
        ans = 0
        visited = {}
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                if cur in visited or cur in dead:
                    continue
                visited[cur] = True
                if cur == target:
                    return ans
                for i in range(4):
                    c = int(cur[i])
                    for x in [-1,1]:
                        nc = (c+x) % 10
                        ncur = cur[:i]+str(nc)+cur[i+1:]
                        q.append(ncur)
            ans += 1
        return -1