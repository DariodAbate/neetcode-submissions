# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        notHb = False

        
        def dfs(root: Optional[TreeNode]) -> int:
            nonlocal notHb 

            if not root:
                return 0

            lh = dfs(root.left)
            dh = dfs(root.right)

            if abs(lh - dh) > 1:
                notHb = True
            
            return 1 + max(
                lh,
                dh
            )

        dfs(root)

        return not notHb