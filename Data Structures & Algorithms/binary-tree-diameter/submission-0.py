# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        stack = []
        stack.append(root)
        d = 0
        while stack:
            n = stack.pop()

            lh = 0
            rh = 0
            if n.left:
                stack.append(n.left)
                lh = self.depthTree(n.left) 
            if n.right:
                stack.append(n.right)
                rh = self.depthTree(n.right) 

            
            d = max(d, lh + rh)
        return d

    def depthTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        
        return 1 + max(
            self.depthTree(root.left),
            self.depthTree(root.right),
        )
        