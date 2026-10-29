# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flatten(self, root: TreeNode | None) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        while root:
            if root.left:
                r = root.right
                nxt = root.left
                while nxt.right:
                    nxt = nxt.right
                root.right = root.left
                root.left = None
                nxt.right = r
            root = root.right
