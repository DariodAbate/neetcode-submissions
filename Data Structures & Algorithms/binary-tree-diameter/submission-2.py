# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    d = 0

    def diameterOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        self.depthTree(root)
        return self.d

    def depthTree(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0
        lh = self.depthTree(root.left)
        dh = self.depthTree(root.right)
        self.d = max(self.d, lh+dh)

        return 1 + max(lh, dh)
        