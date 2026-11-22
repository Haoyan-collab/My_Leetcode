# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import defaultdict,deque
class Solution:
    def addOneRow(self, root: Optional[TreeNode], val: int, depth: int) -> Optional[TreeNode]:
        layers = defaultdict(list)
        q = deque()
        if not root:
            return -1
        
        q.append(root)
        l = 1
        while q:
            for _ in range(len(q)):
                cur = q.popleft()
                layers[l].append(cur)
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
            l += 1
        
        if depth == 1:
            node = TreeNode(val)
            node.left = root
            return node
        
        for n in layers[depth-1]:
            node = TreeNode(val)
            left = n.left
            n.left = node
            node.left = left

            node = TreeNode(val)
            right = n.right
            n.right = node
            node.right = right
        
        return root
