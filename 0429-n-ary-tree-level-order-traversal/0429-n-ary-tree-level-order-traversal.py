"""
# Definition for a Node.
class Node:
    def __init__(self, val: Optional[int] = None, children: Optional[List['Node']] = None):
        self.val = val
        self.children = children
"""
from collections import deque
class Solution:
    def levelOrder(self, root: 'Node') -> List[List[int]]:
        q = deque()
        ans = []
        if root:
            q.append(root)
        while q:
            n = len(q)
            layer = []
            for i in range(n):
                cur = q.popleft()
                if cur:
                    layer.append(cur.val)
                    if cur.children:
                        for c in cur.children:
                            q.append(c)
            ans.append(layer)
        return ans