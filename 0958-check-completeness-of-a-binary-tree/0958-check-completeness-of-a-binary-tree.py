# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def isCompleteTree(self, root: TreeNode | None) -> bool:
        if not root:
            return True
        q = deque()
        q.append(root)
        seen = False
        while q:
            for i in range(len(q)):
                cur = q.popleft()
                if cur is None:
                    if not seen:
                        seen = True
                else:
                    if seen:
                        return False
                    q.append(cur.left)
                    q.append(cur.right)
        return True