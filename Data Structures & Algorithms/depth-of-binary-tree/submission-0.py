# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        if not root:
            return 0

        depth = 1
        queue = deque([(root, depth)])
        while queue:
            n = queue.popleft()

            if n[0].right:
                depth = max(depth, n[1] + 1)
                queue.append((n[0].right, depth))
            
            if n[0].left:
                depth = max(depth, n[1] + 1)
                queue.append((n[0].left, depth))

        return depth

        