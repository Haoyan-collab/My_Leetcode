# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def longestZigZag(self, root: TreeNode | None) -> int:
        if not root:
            return -1
        
        ans = 0
        def dfs(node,flag):
            nonlocal ans
            if not node:
                return 0
            l = dfs(node.left,'left')
            r = dfs(node.right,'right')
            ans = max(ans,l,r)
            if flag == 'left':
                return r+1
            else:
                return l+1
        
        dfs(root,'left')
        dfs(root,'right')
        return ans
        
        