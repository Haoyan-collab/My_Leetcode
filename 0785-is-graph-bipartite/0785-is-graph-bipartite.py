class Solution:
    def isBipartite(self, graph: list[list[int]]) -> bool:
        n = len(graph)
        parent = [i for i in range(n*2)]

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])
            return parent[x]
        
        def union(a,b):
            pa = find(a)
            pb = find(b)
            if pa != pb:
                parent[pb] = pa

        for u in range(n):
            for v in graph[u]:
                if find(u) == find(v):
                    return False
                union(u,v+n)
                union(u+n,v)

        return True
            