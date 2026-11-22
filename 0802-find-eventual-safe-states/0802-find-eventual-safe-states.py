from collections import defaultdict
class Solution:
    def eventualSafeNodes(self, graph: list[list[int]]) -> list[int]:
        ans = []
        # 1:visited_path 2:safe 3:not safe
        color = defaultdict(int)
        for i,g in enumerate(graph):
            if not g:
                color[i] = 2
        
        def dfs(node):
            if color[node]==1:
                return False
            if color[node]==2:
                return True
            if color[node]==3:
                return False
            
            color[node] = 1
            for n in graph[node]:
                if not dfs(n):
                    color[node] = 3
                    return False
            color[node]=2
            return True

        for i in range(len(graph)):
            if dfs(i):
                ans.append(i)
        
        return ans

            

        