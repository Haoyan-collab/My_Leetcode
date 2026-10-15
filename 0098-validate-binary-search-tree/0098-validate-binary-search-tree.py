# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isValidBST(self, root: TreeNode | None) -> bool:
        def dfs(tnode,low,high):
            val = tnode.val
            if val >= high or val <= low:
                return False

            lt, rt = tnode.left, tnode.right
            if lt and rt:
                return lt.val < val and rt.val > val and dfs(lt,low,val) and dfs(rt,val,high)
            
            elif lt:
                return lt.val < val and dfs(lt,low,val)

            elif rt:
                return rt.val > val and dfs(rt,val,high)

            else:
                return True

        return dfs(root,-float('inf'),float('inf'))