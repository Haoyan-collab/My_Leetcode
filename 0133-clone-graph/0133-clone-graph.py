"""
# Definition for a Node.
class Node:
    def __init__(self, val = 0, neighbors = None):
        self.val = val
        self.neighbors = neighbors if neighbors is not None else []
"""

from typing import Optional
from collections import defaultdict
from collections import deque
class Solution:
    def cloneGraph(self, node: Optional['Node']) -> Optional['Node']:
        if node is None:
            return None
        
        cloned = {}
        q = deque()
        q.append(node)
        cloned[node] = Node(node.val)
        while q:
            cur = q.popleft()
            val = cur.val
            neighbors = cur.neighbors
            for n in neighbors:
                if n is not None:
                    if n not in cloned:
                        cloned[n] = Node(n.val)
                        q.append(n)
                    
                    cloned[cur].neighbors.append(cloned[n])

        return cloned[node]

        
        