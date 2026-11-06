# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def sumNumbers(self, root: TreeNode | None) -> int:
        ans = 0
        if not root:
            return 0
        def dfs(node,sm):
            nonlocal ans
            if not node.left and not node.right:
                ans += sm
                return
            if node.left:
                upsm = sm*10+node.left.val
                dfs(node.left,upsm)
            if node.right:
                upsm = sm*10+node.right.val
                dfs(node.right,upsm)
        
        dfs(root,root.val)
        return ans
            