# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        q = deque()
        ans = []
        if root:
            q.append([root,0])
        layers = defaultdict(list)
        while q:
            cur, lay = q.popleft()
            layers[lay].append(cur.val)
            if cur.left is not None:
                q.append([cur.left,lay+1])
            if cur.right is not None:
                q.append([cur.right,lay+1])

        for _,lst in layers.items():
            ans.append(lst)

        return ans