from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        nm = {}
        graph = defaultdict(set)
        for account in accounts:
            name = account[0]
            e = account[1]
            graph[e]
            nm[e] = name
            for i in range(2,len(account)):
                graph[e].add(account[i])
                graph[account[i]].add(e)
                nm[account[i]] = name
        
        ans = []
        visited = {}
        def dfs(e,path):
            if e in visited:
                return
            visited[e] = True
            path.append(e)
            for email in graph[e]:
                dfs(email,path)

        for e in graph.keys():
            if e in visited:
                continue
            path = []
            name = nm[e]
            dfs(e,path)
            ans.append([name]+sorted(path))
        return ans
