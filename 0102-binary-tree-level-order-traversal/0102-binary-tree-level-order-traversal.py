# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def levelOrder(self, root: TreeNode | None) -> list[list[int]]:
        ans = []
        q = deque()
        q.append([root, 0])
        l = defaultdict(list)
        while q:
            cur = q.popleft()
            node, layer = cur[0], cur[1]
            if node:
                l[layer].append(node.val)
                if node.left:
                    q.append([node.left, layer + 1])
                if node.right:
                    q.append([node.right, layer + 1])
        for _,lst in l.items():
            ans.append(lst)
        return ans