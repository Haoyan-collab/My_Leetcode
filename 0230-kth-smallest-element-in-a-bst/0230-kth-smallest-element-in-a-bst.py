# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthSmallest(self, root: TreeNode | None, k: int) -> int:
        self.rank = 0
        self.ans = -1
        def pre_dfs(root):
            if self.rank > k:
                return
            if root.left:
                pre_dfs(root.left)
            self.rank += 1
            if self.rank == k:
                self.ans = root.val
                return
            if root.right:
                pre_dfs(root.right)
            return
        
        pre_dfs(root)
        return self.ans
