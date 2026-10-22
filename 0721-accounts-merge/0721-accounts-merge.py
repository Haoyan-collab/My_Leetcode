from collections import defaultdict
class Solution:
    def accountsMerge(self, accounts: list[list[str]]) -> list[list[str]]:
        graph = defaultdict(set)
        e2name = defaultdict(str)
        for acc in accounts:
            name = acc[0]
            e = acc[1]
            e2name[e] = name
            graph[e]
            for i in range(2,len(acc)):
                graph[e].add(acc[i])
                graph[acc[i]].add(e)
                e2name[acc[i]] = name
        
        visited = set()
        def dfs(e,path):
            if e in visited:
                return
            visited.add(e)
            st = graph[e]
            name = e2name[e]
            path.append(e)
            for mails in st:
                dfs(mails,path)

        ans = []
        for e in graph.keys():
            if e not in visited:
                path = []
                dfs(e,path)
                name = e2name[e]
                ans.append([name]+sorted(path))
        
        return ans