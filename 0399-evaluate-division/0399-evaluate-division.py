class Solution:
    def calcEquation(self, equations: List[List[str]], values: List[float], queries: List[List[str]]) -> List[float]:
        graph = {}
        for i,e in enumerate(equations):
            v = values[i]
            a,b = e
            if a not in graph:
                graph[a] = {}
            graph[a][b] = v
            if b not in graph:
                graph[b] = {}
            graph[b][a] = 1/v
        
        ans = []
        def dfs(cur,target,prod,visited):
            if cur in visited:
                return -1.0
            visited[cur] = 1
            if cur not in graph:
                return -1.0
            if cur == target:
                return prod
            for key,val in graph[cur].items():
                res = dfs(key,target,prod*val,visited)
                if res != -1.0:
                    return res
            return -1.0

        for q in queries:
            a,b = q
            ans.append(dfs(a,b,1.0,{}))
        
        return ans
