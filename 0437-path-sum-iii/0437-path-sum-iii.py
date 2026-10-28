# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def pathSum(self, root: TreeNode | None, targetSum: int) -> int:
        pre = 0
        ans = 0
        def dfs(root,prefix):
            nonlocal pre
            nonlocal ans
            if not root:
                return
            pre += root.val
            target = pre-targetSum
            if target in prefix:
                ans += prefix[target]
            prefix[pre] = prefix.get(pre,0)+1
            dfs(root.left,prefix)
            dfs(root.right,prefix)
            prefix[pre] = prefix.get(pre,0)+-1
            pre -= root.val
            return

        prefix = {0:1}
        if not root:
            return 0

        dfs(root,prefix)
        return ans