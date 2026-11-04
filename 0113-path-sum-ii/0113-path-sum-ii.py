# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> list[list[int]]:
        ans = []
        def dfs(node,path,sm):
            # if not node:
            #     return
            if sm == targetSum and not node.left and not node.right:
                ans.append(path[:])
            if node.left:
                path.append(node.left.val)
                dfs(node.left,path,sm+node.left.val)
                path.pop()
            if node.right:
                path.append(node.right.val)
                dfs(node.right,path,sm+node.right.val)
                path.pop()
            return
        
        if not root:
            return []
        path = [root.val]
        dfs(root,path,root.val)
        return ans