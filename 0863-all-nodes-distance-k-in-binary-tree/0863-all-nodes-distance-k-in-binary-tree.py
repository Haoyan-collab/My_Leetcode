# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None
from collections import deque
class Solution:
    def distanceK(self, root: TreeNode, target: TreeNode, k: int) -> List[int]:
        graph = {}
        def dfs(node):
            if not node:
                return
            v = node.val
            if v not in graph:
                graph[v] = []
            if node.left:
                graph[v].append(node.left.val)
                if node.left.val not in graph:
                    graph[node.left.val] = []
                graph[node.left.val].append(v)
                dfs(node.left)
            if node.right:
                graph[v].append(node.right.val)
                if node.right.val not in graph:
                    graph[node.right.val] = []
                graph[node.right.val].append(v)
                dfs(node.right)
        dfs(root)
        q = deque()
        visited = {target.val:1}
        q.append(target.val)
        steps = 0
        while q:
            if steps == k:
                break
            for _ in range(len(q)):
                cur = q.popleft()
                for n in graph[cur]:
                    if n not in visited:
                        visited[n] = 1
                        q.append(n)
            steps += 1
        if steps == k:
            return list(q)
        return []

