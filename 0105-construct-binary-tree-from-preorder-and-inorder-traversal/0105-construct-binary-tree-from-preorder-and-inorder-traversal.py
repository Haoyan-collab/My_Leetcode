# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def buildTree(self, preorder: list[int], inorder: list[int]) -> TreeNode | None:
        if not preorder:
            return None
        v = preorder[0]
        head = TreeNode(v)
        idx = 0
        while inorder[idx] != v:
            idx += 1
        head.left = self.buildTree(preorder[1:idx+1],inorder[:idx])
        head.right = self.buildTree(preorder[idx+1:],inorder[idx+1:])
        return head
        