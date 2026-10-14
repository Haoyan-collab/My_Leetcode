class Solution:
    def findCircleNum(self, isConnected: List[List[int]]) -> int:
        n = len(isConnected)
        parent = [i for i in range(n)]
        self.ans = n
        def find(x):
            if x != parent[x]:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a,b):
            pa = find(a)
            pb = find(b)

            if pa != pb:
                self.ans -= 1
                parent[pb] = pa


        for i in range(n):
            for j in range(n):
                if isConnected[i][j]:
                    union(i,j)

        return self.ans