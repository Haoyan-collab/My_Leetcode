class Solution:
    def findRedundantConnection(self, edges: list[list[int]]) -> list[int]:
        parent = list(range(len(edges)+1))

        def find(x):
            if parent[x] != x:
                parent[x] = find(parent[x])

            return parent[x]

        def union(a,b):
            pa = find(a)
            pb = find(b)
            if pa == pb:
                return False

            parent[pb] = pa
            return True

        for edge in edges:
            a,b = edge
            if not union(a,b):
                return [a,b]

        return []