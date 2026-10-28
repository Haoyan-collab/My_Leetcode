# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def rightSideView(self, root: TreeNode | None) -> list[int]:
        ans = []
        q = deque()
        if not root:
            return []
        q.append(root)
        while q:
            n = len(q)
            for i in range(n):
                cur = q.popleft()
                if cur.left:
                    q.append(cur.left)
                if cur.right:
                    q.append(cur.right)
                if i == n-1:
                    ans.append(cur.val)
        return ans