# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        posin = {v:i for i,v in enumerate(inorder)}
        idx = 0
        def dfs(left,right):
            nonlocal idx
            if left>right:
                return None
            v = preorder[idx]
            idx += 1
            head = TreeNode(v)
            mid = posin[v]
            head.left = dfs(left,mid-1)
            head.right = dfs(mid+1,right)
            return head
        return dfs(0,len(preorder)-1)