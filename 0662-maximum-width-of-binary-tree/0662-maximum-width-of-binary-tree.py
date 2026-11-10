# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
from collections import deque
class Solution:
    def widthOfBinaryTree(self, root: TreeNode | None) -> int:
        q = deque()
        ans = 0
        if not root:
            return 0
        q.append((root,0))
        while q:
            head = q[0][1]
            fst,lst = -1,-1
            for i in range(len(q)):
                cur,idx = q.popleft()
                idx -= head
                if fst == -1:
                    fst = idx
                lst = idx
                if cur.left:
                    q.append((cur.left,2*idx+1))
                if cur.right:
                    q.append((cur.right,2*idx+2))
            ans = max(ans,lst-fst+1)

        return ans
                
                